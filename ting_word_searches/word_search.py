from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []
    for i in range(len(instance)):
        ocurrencies = []
        data = instance.search(i)
        file_lines = data["linhas_do_arquivo"]
        for index, line in enumerate(file_lines):
            occurency = {}
            if word.lower() in line.lower():
                occurency["linha"] = index + 1
                ocurrencies.append(occurency)
        search_data = dict(
            [
                ("palavra", word),
                ("arquivo", data["nome_do_arquivo"]),
                ("ocorrencias", ocurrencies),
            ]
        )
        if len(search_data["ocorrencias"]):
            result.append(search_data)

    return result


def get_line_content(instance: Queue, line_index: int):
    for i in range(len(instance)):
        data = instance.search(i)
        if data and "linhas_do_arquivo" in data:
            file_lines = data["linhas_do_arquivo"]
            if line_index < len(file_lines):
                return file_lines[line_index]
    return None


def search_by_word(word: str, instance: Queue):
    result = exists_word(word, instance)
    for search_data in result:
        for occurrency in search_data["ocorrencias"]:
            line_index = occurrency["linha"] - 1
            occurrency["conteudo"] = get_line_content(instance, line_index)
    return result
