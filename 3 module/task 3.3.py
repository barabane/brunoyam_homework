# Уровень 1
from math import sqrt


def triangle_area(a, b, c):
    # полупериметр
    p = (a+b+c) / 2

    return sqrt(p*(p-a)*(p-b)*(p-c))


print(triangle_area(15, 13, 17))

# Уровень 2
s = 'одно из чудес русской кухни. Рецепт блинов прост, как и всё гениальное. При этом приготовление блинов — целая наука. А блины на масленицу - один из самых вкусных обычаев. Многих очень интересуют рецепты блинов на масленицу, тесто на блины. Поэтому поговорим о том'


def find_less(string: str):
    res = []
    for word in string.split():
        if len(word) < 5:
            res.append(word)
    return res


print(find_less(s))

# Уровень 3
l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]


def create_max(arr: list):
    arr.sort(reverse=True)
    return arr


print(create_max(l1))
