# Yandex контест ID 80669896
from typing import List, Tuple
from exeptions import EmptyDequeError, DequeIsFullError


class Deque:
    def __init__(self, deque_size: int):
        """Создание объекта класса с длинной deque_size."""
        self.deque = [None] * deque_size
        self.max_size = deque_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """Проверка дека на пустоту."""
        return self.size == 0

    def is_full(self):
        """Проверка дека на предельное заполнение."""
        return self.size == self.max_size

    def push_back(self, value):
        """Добавление элемента в конец дека."""
        if self.size == self.max_size:
            raise DequeIsFullError
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        """Добавление элемента в начало дека."""
        if self.size == self.max_size:
            raise DequeIsFullError
        self.deque[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_front(self):
        """Извлекает элемент из начала дека."""
        if self.is_empty():
            raise EmptyDequeError
        result = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return result

    def pop_back(self):
        """Извлекает элемент c конца дека."""
        if self.is_empty():
            raise EmptyDequeError("Дек пуст")
        result = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return result


def read_input() -> Tuple[int, List[str]]:
    """ Ввод данных."""
    number_of_commands: int = int(input())
    deque_size: int = int(input())
    commands_list: list = []
    for i in range(number_of_commands):
        command = input()
        commands_list.append(command)
    return (deque_size, commands_list)


def get_func_results(deque_size, commands_list):
    """Вывод результатов работы методов дека."""
    deque = Deque(deque_size)
    for i in range(len(commands_list)):
        command, *value = commands_list[i].split()
        try:
            result = getattr(deque, command)(*value)
            if result is not None:
                print(result)
        except Exception as error:
            print("error")


if __name__ == '__main__':
    deque_size, commands_list = read_input()
    get_func_results(deque_size, commands_list)
