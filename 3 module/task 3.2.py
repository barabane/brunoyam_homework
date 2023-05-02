# Уровень 1

from random import randint
l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']

copies = dict()
res = []
for i in l:
    if i not in copies:
        copies[i] = 1
    else:
        copies[i] += 1

for i, j in copies.items():
    if j > 1:
        res.append(i)
print(res)

# Уровень 2

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]

maximum = 0
print(m)

for i in m:
    for j in i:
        if j > maximum:
            maximum = j
print(maximum)

# Уровень 3

d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

new_d = dict()
for i, j in d.items():
    new_d[j] = i

print(new_d)
