# ID успешной посылки 80171504
from typing import Tuple, List


def get_scores(k: int, training_field: List):
    """Подсчет баллов, которые можно набрать на тренажере."""
    number_of_players: int = 2
    scores = {}
    off_limit: set = set()
    for i in training_field:
        if i.isdigit() and i not in off_limit:
            scores[i] = 1 if i not in scores else scores[i] + 1
            if scores[i] > k*number_of_players:
                off_limit.add(i)
                scores.pop(i)
    return len(scores)


def read_input() -> Tuple[int, List]:
    """ Ввод данных."""
    k: int = int(input())
    training_field = []
    for row in range(0, 4):
        row = str(input())
        training_field += row
    return (k, training_field)


if __name__ == "__main__":
    k, training_field = read_input()
    print(get_scores(k, training_field))
