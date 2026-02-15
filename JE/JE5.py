import os
import re
import time
import argparse
import hashlib
from urllib.parse import urljoin, unquote

import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

BASE_SITE = "https://www.justice.gov"
DATASET_PAGE_TMPL = "https://www.justice.gov/epstein/doj-disclosures/data-set-{n}-files"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept": "text/html,application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
}

# Cookie age-gate (vu dans ton Chrome)
COOKIES = {
    "justiceGovAgeVerified": "true"
}

def safe_filename(name: str, max_len: int = 140) -> str:
    """Nettoie un nom de fichier pour Windows/mac/linux."""
    name = unquote(name)  # decode %20 etc
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
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    pix.save(jpg_path)
    doc.close()

def is_pdf_response(first_bytes: bytes) -> bool:
    return first_bytes.startswith(b"%PDF")

def fetch_dataset_pdf_links(dataset_n: int, session: requests.Session) -> list[str]:
    page_url = DATASET_PAGE_TMPL.format(n=dataset_n)
    r = session.get(page_url, headers=HEADERS, cookies=COOKIES, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        # Beaucoup de liens sont relatifs
        abs_url = urljoin(BASE_SITE, href)

        # Heuristiques : on garde les liens .pdf ou ceux contenant /epstein/files/ ... .pdf
        if ".pdf" in abs_url.lower():
            links.add(abs_url)

    # Optionnel: filtrer pour ne garder que les PDFs du dataset demandé si la page mélange
    # (souvent les liens contiennent ".../files/DataSet%2012/..." ou "DataSet 12")
    filtered = []
    ds_pat = re.compile(rf"/epstein/files/.*dataset%20?{dataset_n}\b", re.IGNORECASE)
    for u in sorted(links):
        if ds_pat.search(u) or f"DataSet%20{dataset_n}" in u or f"DataSet {dataset_n}" in unquote(u):
            filtered.append(u)

    # Si le filtre est trop strict (0 résultat), on retombe sur tous les PDFs trouvés.
    return filtered if filtered else sorted(links)

def download_one_pdf(url: str, out_dir: str, session: requests.Session, delay: float, make_jpg: bool, dpi: int) -> tuple[bool, str]:
    os.makedirs(out_dir, exist_ok=True)
    jpg_dir = os.path.join(out_dir, "_previews")
    if make_jpg:
        os.makedirs(jpg_dir, exist_ok=True)

    # Nom depuis l'URL; fallback sur hash si besoin
    base_name = url.split("/")[-1] or "file.pdf"
    base_name = safe_filename(base_name)
    if not base_name.lower().endswith(".pdf"):
        base_name += ".pdf"

    pdf_path = os.path.join(out_dir, base_name)

    # Eviter collisions (même nom sur pages différentes)
    if os.path.exists(pdf_path):
        # on suppose déjà téléchargé
        return True, pdf_path

    try:
        r = session.get(url, headers=HEADERS, cookies=COOKIES, timeout=60, stream=True, allow_redirects=True)
        if r.status_code != 200:
            return False, f"HTTP {r.status_code} {url}"

        it = r.iter_content(chunk_size=8192)
        first = next(it, b"")
        if not is_pdf_response(first):
            # probablement page HTML age-gate / autre
            snippet = first[:200].decode("utf-8", errors="replace").replace("\n", " ")
            return False, f"NOT_PDF {url} | {snippet}"

        with open(pdf_path, "wb") as f:
            f.write(first)
            for chunk in it:
                if chunk:
                    f.write(chunk)

        if make_jpg:
            jpg_path = os.path.join(jpg_dir, base_name[:-4] + ".jpg")
            pdf_first_page_to_jpg(pdf_path, jpg_path, dpi=dpi)

        time.sleep(delay)
        return True, pdf_path

    except Exception as e:
        return False, f"ERR {url} | {e}"

def main():
    ap = argparse.ArgumentParser(description="Scrape DOJ Epstein dataset page, download PDFs, optionally generate JPG preview.")
    ap.add_argument("--dataset", type=int, required=True, help="Dataset number (1..12)")
    ap.add_argument("--out", default="downloads", help="Output folder")
    ap.add_argument("--delay", type=float, default=0.4, help="Delay between downloads (seconds)")
    ap.add_argument("--jpg", action="store_true", help="Generate JPG preview of first page")
    ap.add_argument("--dpi", type=int, default=150, help="DPI for JPG preview")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of PDFs (0 = no limit)")
    args = ap.parse_args()

    if not (1 <= args.dataset <= 12):
        raise SystemExit("dataset must be between 1 and 12")

    dataset_dir = os.path.join(args.out, f"dataset_{args.dataset:02d}")

    with requests.Session() as session:
        print(f"Fetching list for dataset {args.dataset} ...", flush=True)
        pdf_links = fetch_dataset_pdf_links(args.dataset, session)
        if args.limit and args.limit > 0:
            pdf_links = pdf_links[:args.limit]

        print(f"Found {len(pdf_links)} PDF link(s).", flush=True)

        ok = 0
        fail = 0
        for idx, url in enumerate(pdf_links, 1):
            success, info = download_one_pdf(
                url=url,
                out_dir=dataset_dir,
                session=session,
                delay=args.delay,
                make_jpg=args.jpg,
                dpi=args.dpi,
            )
            if success:
                ok += 1
                print(f"[{idx}/{len(pdf_links)} OK] {os.path.basename(info)}", flush=True)
            else:
                fail += 1
                print(f"[{idx}/{len(pdf_links)} FAIL] {info}", flush=True)

        print(f"Done. OK={ok} FAIL={fail}. Output: {dataset_dir}", flush=True)

if __name__ == "__main__":
    main()

# py .\JE5.py --dataset 12 --jpg --limit 10