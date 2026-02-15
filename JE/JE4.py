import os
import time
import requests
import fitz  # PyMuPDF

# il y a 12 datasets

BASE_URL = "https://www.justice.gov/epstein/files/DataSet%212/EFTA"
PDF_DIR = "downloads"
JPG_DIR = "previews"

START = 1
END = 10
DELAY = 0.3

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(JPG_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
}

COOKIES = {
    "justiceGovAgeVerified": "true"
}

def format_num(n: int) -> str:
    return f"{n:08d}"  # 00000001

def pdf_first_page_to_jpg(pdf_path: str, jpg_path: str, dpi: int = 150) -> None:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # première page
    zoom = dpi / 72  # 72 dpi base
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    pix.save(jpg_path)
    doc.close()

def download_pdf_and_preview(n: int) -> bool:
    num = format_num(n)
    url = f"{BASE_URL}{num}.pdf"
    pdf_path = os.path.join(PDF_DIR, f"EFTA{num}.pdf")
    jpg_path = os.path.join(JPG_DIR, f"EFTA{num}.jpg")

    try:
        r = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=30, stream=True, allow_redirects=True)
        if r.status_code != 200:
            print(f"[SKIP {r.status_code}] {num}")
            return False

        # Vérif signature PDF
        it = r.iter_content(chunk_size=8192)
        first = next(it, b"")
        if not first.startswith(b"%PDF"):
            print(f"[AGE-GATE/NOT_PDF] {num} -> {r.url}")
            return False

        # Écrit le PDF
        with open(pdf_path, "wb") as f:
            f.write(first)
            for chunk in it:
                if chunk:
                    f.write(chunk)

        # Génère le JPG (page 1)
        pdf_first_page_to_jpg(pdf_path, jpg_path, dpi=150)

        print(f"[OK] {num} -> PDF+JPG")
        return True

    except Exception as e:
        print(f"[ERR] {num} — {e}")
        return False

def main():
    print("Démarrage...")
    for i in range(START, END + 1):
        download_pdf_and_preview(i)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
