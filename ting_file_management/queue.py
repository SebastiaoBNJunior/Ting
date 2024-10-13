from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __str__(self) -> str:
        str_items = ""
        for i in range(len(self._data)):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < len(self._data):
                str_items += ", "

        return f"Queue({str_items})"

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None

        return self._data.pop(0)

    def search(self, index):
        if 0 <= index <= len(self._data) - 1:
            return self._data[index]
        raise IndexError("Índice Inválido ou Inexistente")
