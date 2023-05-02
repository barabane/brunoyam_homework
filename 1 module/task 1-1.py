# Модуль 1 часть 1

# Уровень 1
answer = (5 + (7*5/8)) / 3**5
print('значение выражения:', answer)


# Уровень 2
speed = int(input('введите скорость:'))
time = int(input('введите кол-во часов:'))

summ = speed * time
if speed * time < 109:
    print(f'Вася остановиться на отметке: {speed * time} км')
else:
    answer = 0
    while summ > 109:
        summ -= 109
        answer += summ
    print(f'Вася остановиться на отметке: {answer} км')


# Уровень 3
n1 = float(input('введите 1 число:'))
n2 = float(input('введите 2 число:'))

print(n1 if n1 > n2 else n2)
