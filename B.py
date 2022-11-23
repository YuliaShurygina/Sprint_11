# Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
#  В нём на каждом раунде появляется конфигурация цифр и точек.
# На клавише написана либо точка, либо цифра от 1 до 9.
# В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t.
#  Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
# Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.
# Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.
# Формат ввода
# В первой строке дано целое число k (1 ≤ k ≤ 5).
# В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке.
# Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.
# Формат вывода
# Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.
from typing import Dict, Tuple


def count_unique_symbols(input_string: str) -> Dict[str, int]:
    """Находим и подсчитываем уникальные символы, за исключением '.'."""
    unique_symbols: Dict[str, int] = {}
    for char in input_string:
        if char != '.':
            if char in unique_symbols:
                unique_symbols[char] += 1
            else:
                unique_symbols[char] = 1
    return unique_symbols


def find_score(unique_symbols: Dict[str, int], k: int) -> int:
    """Находим количество баллов."""
    score: int = 0
    for i in unique_symbols.values():
        if i <= 2*k:
            score += 1
    return score


def read_input() -> Tuple[str, int]:
    """Считываем  данные."""
    k: int = int(input())
    total_str = "".join(input().strip() for _ in range(4))
    return total_str, k


def main():
    total_str, k = read_input()
    unique_symbols = count_unique_symbols(total_str)
    print(find_score(unique_symbols, k))


if __name__ == '__main__':
    main()
