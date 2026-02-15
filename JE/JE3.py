import os
import time
import requests

print("TOP: script chargé")

BASE_URL = "https://www.justice.gov/epstein/files/DataSet%201/EFTA"
SAVE_DIR = "downloads"
START = 1
END = 50
DELAY = 0.3

os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
}

COOKIES = {
    "justiceGovAgeVerified": "true"
}


def format_num(n):
    return f"{n:08d}"

def download_pdf(n):
    num = format_num(n)
    url = f"{BASE_URL}{num}.pdf"

    try:
        r = requests.get(
            url,
            headers=HEADERS,
            cookies=COOKIES,
            timeout=30,
            stream=True,
            allow_redirects=True
        )

        if r.status_code != 200:
            print(f"[SKIP {r.status_code}] {num}")
            return False

        first = next(r.iter_content(8192), b"")

        if not first.startswith(b"%PDF"):
            print(f"[AGE-GATE] {num}")
            return False

        path = os.path.join(SAVE_DIR, f"EFTA{num}.pdf")
        with open(path, "wb") as f:
            f.write(first)
            for chunk in r.iter_content(1024 * 256):
                if chunk:
                    f.write(chunk)

        print(f"[OK] {num}")
        return True

    except Exception as e:
        print(f"[ERR] {num} {e}")
        return False

def main():
    print("Démarrage...")
    for i in range(START, END + 1):
        download_pdf(i)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
