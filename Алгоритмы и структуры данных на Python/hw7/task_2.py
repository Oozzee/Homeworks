# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1


N = 50
SIZE = 10
arr = [round(random.uniform(0, N), 2) for _ in range(SIZE)]
print(arr)

mergeSort(arr)

print(arr)
