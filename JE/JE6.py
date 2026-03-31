import os
import re
import time
import argparse
import random
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse, unquote

import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF


BASE_SITE = "https://www.justice.gov"
DATASET_PAGE_TMPL = "https://www.justice.gov/epstein/doj-disclosures/data-set-{n}-files"

BASE_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
}


COOKIE_HEADER = "_ga=GA1.1.1922119951.1771051436; nmstat=9c193466-afd7-91d7-ad17-f508a838ff51; justiceGovAgeVerified=true; ak_bmsc=B79E90E436B47B296AD6CCE7D983A135~000000000000000000000000000000~YAAQoQcQAv2xGlGcAQAAM07qXR7nibGHr/o/sGyo2vIWW0KPS2C5d56waoKm2FTzKJ8ucf0UNQkweKDd/ba+Svp3tRh7WB/ExyMAhVg7UXDrrXK8zPXVt4nBYFdkyoQbTO2p/1PBMYOt7HZrssEtY0R9kiKk6BhHXpbda6ObT3hPCr3uQuPaYM7tzjgpFFg7fMJYEgIZCFUOlEXmiGlXnfe+KxnkYrwyCzBitiEaTa0fZq43tm7O63sCQtlbyqoBonRYKb74Aene2dkm6pI6cUhLRmKRzXNVDSfBTtGGmfTuC7Ez/T72URpVntLADyEi5ZLgnFN0ewQ9nEA3IeAs42a02Ayh0sykfVRvpU+bgJYKr59RAMVdlvLKN3sOaFIeIVet7HRJ1kFsGtVmzEcb7Jx5t0AWks6chVxmkzZQijc4kLDu8c05rgnMqG15TZQzuPyNrtTZbhHyj4IebCha43pQcwtcFTr/; QueueITAccepted-SDFrts345E-V3_usdojfiles=EventId%3Dusdojfiles%26RedirectType%3Dsafetynet%26IssueTime%3D1771102990%26Hash%3D81a7c07c340b8553d2ed2f6835266c90b7b28c8dc8d34ab03cce9b006be158a8; _ga_CSLL4ZEK4L=GS2.1.s1771101574$o2$g1$t1771104761$j41$l0$h0"



def safe_filename(name: str, max_len: int = 160) -> str:
    name = unquote(name)
    name = name.strip().replace("\n", " ").replace("\r", " ")
    name = re.sub(r"[<>:\"/\\|?*\x00-\x1F]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    if len(name) > max_len:
        root, dot, ext = name.rpartition(".")
        if dot:
            name = root[: max_len - (len(ext) + 1)] + "." + ext
        else:
            name = name[:max_len]
    return name

def pdf_first_page_to_jpg(pdf_path: str, jpg_path: str, dpi: int = 150) -> None:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    zoom = dpi / 72
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    pix.save(jpg_path)
    doc.close()

def is_pdf_bytes(first_bytes: bytes) -> bool:
    return first_bytes.startswith(b"%PDF")

def with_page(url: str, page: int) -> str:
    parts = urlparse(url)
    q = parse_qs(parts.query)
    q["page"] = [str(page)]
    new_query = urlencode(q, doseq=True)
    return urlunparse((parts.scheme, parts.netloc, parts.path, parts.params, new_query, parts.fragment))

def extract_pdf_links(soup: BeautifulSoup) -> list[str]:
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        abs_url = urljoin(BASE_SITE, href)
        if ".pdf" in abs_url.lower():
            links.append(abs_url)
    return links

def detect_max_page(soup: BeautifulSoup) -> int:
    max_page = 0
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "page=" in href:
            try:
                qs = parse_qs(urlparse(urljoin(BASE_SITE, href)).query)
                if "page" in qs and qs["page"]:
                    p = int(qs["page"][0])
                    max_page = max(max_page, p)
            except Exception:
                pass
    return max_page

def get_with_retries(session: requests.Session, url: str, referer: str | None, timeout: int = 30, tries: int = 5):
    """
    GET robuste avec Referer + backoff.
    Retourne toujours une Response, sinon lève une exception.
    """
    last_resp = None
    last_exc = None


    for attempt in range(1, tries + 1):
        headers = dict(BASE_HEADERS)
        if referer:
            headers["Referer"] = referer

        try:
            headers["cookie"] = COOKIE_HEADER
            resp = session.get(url, headers=headers, timeout=timeout, allow_redirects=True)
            last_resp = resp

            # 403 => backoff puis retry
            if resp.status_code == 403:
                sleep_s = (1.5 * attempt) + random.uniform(0.2, 0.8)
                time.sleep(sleep_s)
                continue

            return resp

        except Exception as e:
            last_exc = e
            time.sleep(1.0 * attempt)

    # Si on sort de la boucle, on échoue : on lève une erreur claire
    if last_resp is not None:
        raise requests.HTTPError(f"Failed after {tries} tries. Last status={last_resp.status_code} url={url}")
    if last_exc is not None:
        raise RuntimeError(f"Failed after {tries} tries. Last exception={last_exc} url={url}")

    raise RuntimeError(f"Failed after {tries} tries. Unknown error. url={url}")


def fetch_dataset_pdf_links(dataset_n: int, session: requests.Session, limit: int = 0, verbose: bool = True) -> list[str]:
    base_url = DATASET_PAGE_TMPL.format(n=dataset_n)

    # Page 0
    url0 = with_page(base_url, 0)
    r0 = get_with_retries(session, url0, referer=None, timeout=30, tries=4)
    r0.raise_for_status()
    soup0 = BeautifulSoup(r0.text, "html.parser")
    max_page = detect_max_page(soup0)

    if verbose:
        print(f"Pagination détectée: pages 0..{max_page}", flush=True)

    pdf_links = []
    seen = set()

    # Parcours page=0..max_page en mettant le referer sur la page précédente
    prev_url = None
    for page in range(0, max_page + 1):
        page_url = with_page(base_url, page)
        r = get_with_retries(session, page_url, referer=prev_url, timeout=30, tries=5)


        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        page_links = extract_pdf_links(soup)
        new_on_page = 0
        for u in page_links:
            if u not in seen:
                seen.add(u)
                pdf_links.append(u)
                new_on_page += 1
                if limit and len(pdf_links) >= limit:
                    if verbose:
                        print(f"Page {page}: +{new_on_page} (stop limit={limit})", flush=True)
                    return pdf_links

        if verbose:
            print(f"Page {page}: trouvés {len(page_links)} liens PDF, nouveaux {new_on_page}, total {len(pdf_links)}", flush=True)

        prev_url = page_url
        time.sleep(0.6 + random.uniform(0.0, 0.4))  # petite pause "humaine"

    return pdf_links

def download_one_pdf(url: str, out_dir: str, session: requests.Session, delay: float, make_jpg: bool, dpi: int) -> tuple[bool, str]:
    os.makedirs(out_dir, exist_ok=True)
    jpg_dir = os.path.join(out_dir, "_previews")
    if make_jpg:
        os.makedirs(jpg_dir, exist_ok=True)

    base_name = safe_filename(url.split("/")[-1] or "file.pdf")
    if not base_name.lower().endswith(".pdf"):
        base_name += ".pdf"

    pdf_path = os.path.join(out_dir, base_name)
    jpg_path = os.path.join(jpg_dir, base_name[:-4] + ".jpg")

       # Skip si déjà présent
    if os.path.exists(pdf_path):
        if make_jpg:
            if os.path.exists(jpg_path):
                return True, pdf_path   # PDF + JPG déjà présents
            else:
                # PDF présent mais JPG manquant -> on génère seulement le JPG
                try:
                    pdf_first_page_to_jpg(pdf_path, jpg_path, dpi=dpi)
                    return True, pdf_path
                except Exception as e:
                    return False, f"JPG_FAIL {pdf_path} | {e}"
        else:
            return True, pdf_path


    try:
        # Pour les PDFs, on met un referer sur la page dataset (souvent mieux)
        headers = dict(BASE_HEADERS)
        headers["Accept"] = "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8"

        headers["cookie"] = COOKIE_HEADER
        r = session.get(url, headers=headers, timeout=60, stream=True, allow_redirects=True)
        if r.status_code != 200:
            return False, f"HTTP {r.status_code} {url}"

        it = r.iter_content(chunk_size=8192)
        first = next(it, b"")

        if not is_pdf_bytes(first):
            snippet = first[:200].decode("utf-8", errors="replace").replace("\n", " ")
            return False, f"NOT_PDF {url} | {snippet}"

        with open(pdf_path, "wb") as f:
            f.write(first)
            for chunk in it:
                if chunk:
                    f.write(chunk)

        if make_jpg:
            pdf_first_page_to_jpg(pdf_path, jpg_path, dpi=dpi)

        time.sleep(delay)
        return True, pdf_path

    except Exception as e:
        return False, f"ERR {url} | {e}"

def main():
    ap = argparse.ArgumentParser(description="Scrape DOJ Epstein dataset pages (?page=0..), download PDFs, optionally generate JPG previews.")
    ap.add_argument("--dataset", type=int, required=True, help="Dataset number (1..12)")
    ap.add_argument("--out", default="downloads", help="Output folder")
    ap.add_argument("--delay", type=float, default=0.5, help="Delay between PDF downloads (seconds)")
    ap.add_argument("--jpg", action="store_true", help="Generate JPG preview of first page")
    ap.add_argument("--dpi", type=int, default=150, help="DPI for JPG preview")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of PDFs to download (0 = no limit)")
    args = ap.parse_args()

    if not (1 <= args.dataset <= 12):
        raise SystemExit("dataset must be between 1 and 12")

    dataset_dir = os.path.join(args.out, f"dataset_{args.dataset:02d}")

    with requests.Session() as session:
        print(f"Fetching links for dataset {args.dataset} ...", flush=True)
        pdf_links = fetch_dataset_pdf_links(args.dataset, session, limit=args.limit, verbose=True)
        print(f"Total liens PDF retenus: {len(pdf_links)}", flush=True)

        ok = 0
        fail = 0

        for i, url in enumerate(pdf_links, 1):
            success, info = download_one_pdf(
                url=url,
                out_dir=dataset_dir,
                session=session,
                delay=args.delay,
                make_jpg=args.jpg,
                dpi=args.dpi
            )
            if success:
                ok += 1
                print(f"[{i}/{len(pdf_links)} OK] {os.path.basename(info)}", flush=True)
            else:
                fail += 1
                print(f"[{i}/{len(pdf_links)} FAIL] {info}", flush=True)

        print(f"Done. OK={ok} FAIL={fail}. Output: {dataset_dir}", flush=True)

if __name__ == "__main__":
    main()

# py .\JE6.py --dataset 12 --jpg --limit 60 --delay 0.8

# Réseau → clic droit sur data-set-12-files?page=1 → Copy as cURL
# et tu remplaces uniquement la valeur de COOKIE_HEADER par le nouveau -b "...".