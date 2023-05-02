# Модуль 1 часть 2

# Уровень 1
n1 = int(input('введите 1 число '))
n2 = int(input('введите 2 число '))
n3 = int(input('введите 3 число '))

nums = [n1, n2, n3]
copies = {}
for num in nums:
    copies[num] = num
if len(copies) == 1:
    print(3)
elif len(copies) == 2:
    print(2)
elif len(copies) == 3:
    print(0)


# Уровень 2
v1 = input('столбец 1:')
h1 = input('строка 1:')
v2 = input('столбец 2:')
h2 = input('строка 2:')

if v1 == v2:
    print('YES')
elif h1 == h2:
    print('YES')
else:
    print('NO')

# Уровень 3

while True:
    password = input('введите пароль:')
    if len(password) <= 8:
        print('длина пароля меньше 8 символов')
    elif not sum(1 for ch in password if ch.isupper()):
        print('строка должна содержать хотя бы 1 заглавную букву')
    elif not sum(1 for ch in password if ch.islower()):
        print('строка должна содержать хотя бы 1 прописную букву')
    else:
        break
