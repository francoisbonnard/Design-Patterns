import os
import time
import requests

BASE_URL = "https://www.justice.gov/epstein/files/DataSet%201/EFTA"
SAVE_DIR = "downloads"
START = 1
END = 1000         # commence petit
DELAY = 0.2

os.makedirs(SAVE_DIR, exist_ok=True)

def format_num(n: int) -> str:
    return f"{n:08d}"  # 00000001

def download_pdf(n: int) -> bool:
    num = format_num(n)
    url = f"{BASE_URL}{num}.pdf"

    try:
        # HEAD d'abord (moins lourd). Certains serveurs bloquent HEAD -> on fallback GET.
        r = requests.head(url, timeout=10, allow_redirects=True)
        if r.status_code == 200:
            r = requests.get(url, timeout=20, stream=True, allow_redirects=True)

        if r.status_code == 200 and "pdf" in r.headers.get("Content-Type", "").lower():
            path = os.path.join(SAVE_DIR, f"EFTA{num}.pdf")
            with requests.get(url, timeout=20, stream=True, allow_redirects=True) as g:
                g.raise_for_status()
                with open(path, "wb") as f:
                    for chunk in g.iter_content(chunk_size=1024 * 256):
                        if chunk:
                            f.write(chunk)
            print(f"[OK] {num}")
            return True

        print(f"[SKIP {r.status_code}] {num}")
        return False

    except Exception as e:
        print(f"[ERR] {num} — {e}")
        return False

def main():
    print("Démarrage...")
    for i in range(START, END + 1):
        download_pdf(i)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
