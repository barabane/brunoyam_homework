# Уровень 1

x = float(input())
y = float(input())
p = float(input())

summ = x
years = 0
while summ < y:
    summ = summ + (summ / 100 * p)
    years += 1

print(years)

# Уровень 2

n = int(input('введите кол-во повторений '))

while n > 0:
    print('for - частный случай цикла while')
    n -= 1

# Уровень 3
num = input('введите число')

l = list(str(num))
summ = 0

for i in l:
    summ += int(i)
print(summ)
