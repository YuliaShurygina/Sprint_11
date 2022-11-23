# Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, 
# имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
#  Каждый участок либо пустой, либо на нём уже построен дом.
# Общительный Тимофей не хочет жить далеко от других людей на этой улице. 
# Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. 
# Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
# Помогите Тимофею посчитать искомые расстояния. 
# Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке,
#  в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны
#  n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. 
# Номера домов (положительные числа) уникальны и не превосходят 109.
# Формат вывода
# Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
from typing import List, Tuple

EMPTY_SPACE: int = 0
ZERO_DISTANCE: int = 0


def find_zero_indexes(numbers: List[int], street_length: int) -> List[int]:
    """Создаем список индексов необходимого элемента (в нашем случае 0)."""
    zero_indexes: List[int] = []
    for i in range(street_length):
        if numbers[i] == EMPTY_SPACE:
            zero_indexes.append(i)
    return zero_indexes


def find_distance(numbers: List[int],
                  zero_indexes: List[int], street_length: int) -> List[int]:
    """Находим ближайшее расстояние от каждого элемента до пустого участка."""
    distance: List[int] = []
    zero_mark: int = 0
    first_zero_index: int = 0
    second_zero_index: int = zero_indexes[zero_mark]
    for index in range(street_length):
        if numbers[index] == EMPTY_SPACE:
            distance.append(ZERO_DISTANCE)
            first_zero_index = index
            zero_mark += 1
            if zero_mark >= len(zero_indexes):
                second_zero_index = 0
            else:
                second_zero_index = zero_indexes[zero_mark]
        else:
            if zero_mark == 0:
                distance.append(second_zero_index - index)
            else:
                distance.append(min(abs(first_zero_index-index),
                                abs(second_zero_index - index)))
    return distance


def read_input() -> Tuple[List[int], int]:
    """Считывание данных."""
    street_length: int = int(input())
    numbers: List[int] = [int(x) for x in input().strip().split()]
    return numbers, street_length


def main():
    numbers, street_length = read_input()
    zero_indexes = find_zero_indexes(numbers, street_length)
    print(*find_distance(numbers, zero_indexes, street_length))


if __name__ == '__main__':
    main()
