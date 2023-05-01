# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

n = int(input('Введите размер массива:'))
x = int(input('Введите число:'))
array = [random.randrange(1,10) for i in range(1,n + 1)]
diff = abs(x - array[0])
index = 0
for i in range(len(array)):
    count = abs(x - array[i])
    if count < diff:
        diff = count
        index = i
print(array)
print(array[index])