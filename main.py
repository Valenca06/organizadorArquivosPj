from collections import defaultdict
import hashlib
from pathlib import Path
import shutil

pasta = Path.cwd()
grupos = defaultdict(list)

for arq in pasta.iterdir():
    if arq.is_file():
        grupos[hashlib.md5(arq.read_bytes()).hexdigest()].append(arq)

for files in grupos.values():
    if len(files) > 1:
        orig, *dups = files
        qtd = len(dups)

        print(f"\nOriginal: {orig.name}")
        print("Duplicatas: " + ", ".join(d.name for d in dups))

        resp_todas = input(f"Apagar TODAS as {qtd} duplicatas? (s/n): ").strip().lower()

        if resp_todas == "s":
            for d in dups:
                d.unlink()
                print(f"  -> Apagado: {d.name}")
        else:
            for d in dups:
                resp_ind = input(f"  Apagar '{d.name}'? (s/n): ").strip().lower()
                if resp_ind == "s":
                    d.unlink()
                    print(f"  -> Apagado: {d.name}")

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documentos": [".docx", ".txt", ".xlsx", ".csv"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mkv"],
    "Audios": [".mp3", ".wav"],
}
EXT_MAP = {ext: cat for cat, exts in CATEGORIAS.items() for ext in exts}

for arq in pasta.iterdir():
    if arq.is_file() and arq.suffix.lower() not in (".py", ".exe"):
        cat = EXT_MAP.get(arq.suffix.lower(), "Outros")
        dest = pasta / cat
        dest.mkdir(exist_ok=True)
        shutil.move(str(arq), str(dest / arq.name))
        print(f"Movido: {arq.name} -> [{cat}]")

input("\nProcesso concluído! Pressione ENTER...")