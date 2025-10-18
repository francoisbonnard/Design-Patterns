import argparse
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse, unquote

MD_IMG_REGEX = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
HTML_IMG_REGEX = re.compile(r'<img[^>]*\bsrc=[\'"]([^\'"]+)[\'"][^>]*>', re.IGNORECASE)

IMAGE_EXTS = {'.png', '.jpg', '.jpeg'}

def is_web_url(s: str) -> bool:
    try:
        scheme = urlparse(s).scheme.lower()
        return scheme in ('http', 'https', 'data')
    except Exception:
        return False

def normalize_link_target(raw: str) -> str:
    # Enlève titres "title" éventuels après l'URL:  (path "title")
    # et strips < > éventuels.
    s = raw.strip()
    if s.startswith('<') and s.endswith('>'):
        s = s[1:-1].strip()
    # Retire un éventuel titre markdown à la fin
    # Exemple: image.png "Titre"
    if '"' in s or "'" in s:
        # naive split on first quote if space before it
        parts = re.split(r'\s+(?=["\'])', s, maxsplit=1)
        s = parts[0]
    return s

def unique_destination(dest_dir: Path, base_name: str) -> Path:
    target = dest_dir / base_name
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    i = 1
    while True:
        candidate = dest_dir / f"{stem}-{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def move_image(source_path: Path, img_dir: Path, dry_run: bool) -> Path:
    img_dir.mkdir(parents=True, exist_ok=True)
    target = unique_destination(img_dir, source_path.name)
    if dry_run:
        return target
    shutil.move(str(source_path), str(target))
    return target

def relpath_from_md(md_file: Path, target_path: Path) -> str:
    # Chemin relatif du .md vers le fichier dans ./img
    return os.path.relpath(target_path, start=md_file.parent).replace('\\', '/')

def process_md_file(md_file: Path, root_dir: Path, img_dir: Path, dry_run: bool) -> bool:
    original_text = md_file.read_text(encoding='utf-8', errors='ignore')
    text = original_text

    # Collecte toutes les occurrences (markdown + html)
    replacements = []

    # Markdown image syntax
    for m in MD_IMG_REGEX.finditer(text):
        alt, raw_target = m.group(1), m.group(2)
        target = normalize_link_target(raw_target)
        if is_web_url(target):
            continue
        # Décode %20 etc.
        target_decoded = unquote(target)
        # Résout par rapport au dossier du .md
        source_path = (md_file.parent / Path(target_decoded)).resolve()
        if not source_path.exists() or source_path.is_dir():
            continue
        if source_path.suffix.lower() not in IMAGE_EXTS:
            continue

        # Si déjà dans img_dir (où qu’il soit), seulement réécrire le lien proprement
        if img_dir in source_path.parents or source_path == img_dir:
            new_path = relpath_from_md(md_file, source_path)
            replacements.append((m.span(2), new_path))
            continue

        # Déplacement
        dest_path = move_image(source_path, img_dir, dry_run)
        new_path = relpath_from_md(md_file, dest_path)
        replacements.append((m.span(2), new_path))

    # HTML <img>
    for m in HTML_IMG_REGEX.finditer(text):
        raw_target = m.group(1)
        target = normalize_link_target(raw_target)
        if is_web_url(target):
            continue
        target_decoded = unquote(target)
        source_path = (md_file.parent / Path(target_decoded)).resolve()
        if not source_path.exists() or source_path.is_dir():
            continue
        if source_path.suffix.lower() not in IMAGE_EXTS:
            continue

        if img_dir in source_path.parents or source_path == img_dir:
            new_path = relpath_from_md(md_file, source_path)
            replacements.append((m.span(1), new_path))
            continue

        dest_path = move_image(source_path, img_dir, dry_run)
        new_path = relpath_from_md(md_file, dest_path)
        replacements.append((m.span(1), new_path))

    if not replacements:
        return False

    # Appliquer remplacements de la fin vers le début pour conserver les offsets
    replacements.sort(key=lambda x: x[0][0], reverse=True)
    text_list = list(text)
    for (start, end), new_target in replacements:
        text_list[start:end] = new_target
    new_text = ''.join(text_list)

    if not dry_run and new_text != original_text:
        backup = md_file.with_suffix(md_file.suffix + '.bak')
        md_file.write_text(new_text, encoding='utf-8')
        # Optionnel: garder une sauvegarde
        backup.write_text(original_text, encoding='utf-8')

    return new_text != original_text

def main():
    parser = argparse.ArgumentParser(
        description="Déplace les images référencées dans les .md vers ./img et met à jour les liens."
    )
    parser.add_argument("--root", default=".", help="Dossier racine (par défaut: .)")
    parser.add_argument("--img-dir", default="./img", help="Dossier destination des images (par défaut: ./img)")
    parser.add_argument("--dry-run", action="store_true", help="Ne rien écrire/déplacer, juste simuler")
    parser.add_argument("--ext", nargs="*", default=[".md"], help="Extensions de fichiers Markdown (défaut: .md)")
    args = parser.parse_args()

    root_dir = Path(args.root).resolve()
    img_dir = (root_dir / args.img_dir).resolve()

    changed_files = 0
    for ext in args.ext:
        for md_file in root_dir.rglob(f"*{ext}"):
            if md_file.is_file():
                if process_md_file(md_file, root_dir, img_dir, args.dry_run):
                    changed_files += 1
                    print(f"[OK] {md_file}")

    print(f"Terminé. Fichiers modifiés: {changed_files}. Dry-run: {args.dry_run}")

if __name__ == "__main__":
    main()
