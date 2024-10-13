from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = [
    {
        "nome_do_arquivo": "file_1.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ["a", "b", "c", "d", "e", "f", "g"],
    },
    {
        "nome_do_arquivo": "file_2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["a", "b"],
    },
    {
        "nome_do_arquivo": "file_3.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["linha 1", "linha 2", "linha 3", "linha 4"],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue(mock[0])
    priority_queue.enqueue(mock[1])

    assert len(priority_queue) == 2
    assert priority_queue.search(0) == mock[1]

    priority_queue.enqueue(mock[2])
    assert priority_queue.search(1) == mock[2]

    priority_queue.dequeue()
    assert priority_queue.search(0) == mock[2]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(10)
