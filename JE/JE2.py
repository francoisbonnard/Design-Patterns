import requests
from bs4 import BeautifulSoup
import os

BASE_PAGE = "https://www.justice.gov/epstein/files/DataSet%201/"
SAVE_DIR = "downloads"

os.makedirs(SAVE_DIR, exist_ok=True)

print("Récupération de la page...")

r = requests.get(BASE_PAGE)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

pdf_links = [
    link.get("href")
    for link in links
    if link.get("href") and link.get("href").lower().endswith(".pdf")
]

print(f"{len(pdf_links)} fichiers trouvés.")

for url in pdf_links:
    filename = url.split("/")[-1]
    full_url = url if url.startswith("http") else BASE_PAGE + filename

    print("Téléchargement:", filename)

    file = requests.get(full_url)
    with open(os.path.join(SAVE_DIR, filename), "wb") as f:
        f.write(file.content)

print("Terminé.")
