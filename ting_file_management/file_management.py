import sys


def txt_importer(path_file):
    extension = path_file.split(".")[-1]
    if extension != "txt":
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as txt_file:
            data = txt_file.read().split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    return data
