import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    dictionary = dict(
        [
            ("nome_do_arquivo", path_file),
            ("qtd_linhas", len(data)),
            ("linhas_do_arquivo", data),
        ]
    )
    instance.enqueue(dictionary)
    sys.stdout.write(str(dictionary))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    removed = instance.dequeue()
    path_file = removed["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        return sys.stdout.write(str(data))
    except IndexError:
        return sys.stderr.write("Posição inválida")
