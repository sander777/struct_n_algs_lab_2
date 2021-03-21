# arr = list(map(lambda x: int(x), input().split(' ')))
import random

arr = []
for i in range(10):
    arr.append(random.randint(1, 20))
    arr.append(random.randint(-20, 1))

random.shuffle(arr)
arr.append(0)
m, M = 10000, 0
m_pos, M_pos = 0, 0

p = 0
for i in arr:
    if i == 0:
        break
    if abs(i) > abs(M) and i < 0:
        M = i
        M_pos = p
    if abs(i) < abs(m) and i < 0:
        m = i
        m_pos = p
    p += 1
print(arr)
print(f"Найменший = {m} на позиції {m_pos}\nНайбільший = {M} на позиції {M_pos}")