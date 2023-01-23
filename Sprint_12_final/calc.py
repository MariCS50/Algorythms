# Yandex контест ID 80670499
class Stack:
    def __init__(self):
        """Создание объекта класса стэк."""
        self.items = []

    def push(self, item):
        """Добавление элемента в стэк."""
        self.items.append(item)

    def pop(self):
        """Извлечение элемента из стэка."""
        if len(self.items) == 0:
            raise ValueError("Cтэк пуст")
        return self.items.pop()


def read_input() -> str:
    """ Ввод данных."""
    expression = str(input())
    return expression


def get_calculation(expression: str) -> int:
    """Вычисление результата математических действий."""
    dictionary = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y//x
    }
    result = Stack()
    for i in expression.split(' '):
        try:
            result.push(int(i))
        except ValueError:
            result.push(dictionary[i](result.pop(), result.pop()))
    return result.pop()


if __name__ == '__main__':
    expression = read_input()
    print(get_calculation(expression))
