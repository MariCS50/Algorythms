# ID успешной посылки 80171760
from typing import List


def get_nearest_zero_distance(street_map: List[int]) -> List[int]:
    """ Расчет расстояния до ближайшего нуля."""
    zero_indices = [i for i, x in enumerate(street_map) if x == 0]
    res = []
    if zero_indices[0] != 0:
        res += [i for i in range(zero_indices[0], -1, -1)]
    else:
        res += [0]
    if len(zero_indices) != 1:
        middle_distance = [
            abs(j-i-1) for i, j in zip(zero_indices, zero_indices[1:])
        ]
        for j in middle_distance:
            if j > 0:
                res += [i for i in range(1, (j+1)//2+1)]
                res += [i for i in range(0, (j)//2+1)][::-1]
            else:
                res += [0]
    if zero_indices[-1] < len(street_map)-1:
        res += [i for i in range(1, len(street_map)-zero_indices[-1])]
    return res


def read_input() -> List[int]:
    """ Ввод данных."""
    street_map = [int(num) for num in input().split()]
    return street_map


if __name__ == "__main__":
    street_map = read_input()
    print(*get_nearest_zero_distance(street_map), sep=(' '))
