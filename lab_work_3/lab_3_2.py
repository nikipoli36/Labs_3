import array

n = int(input("Введите размерность массива >> "))
arr = [0] * n

for i in range(len(arr)):
    arr[i] = int(input("Введите значение ячейки массива >> "))

max_i = arr.index(max(arr))
min_i = arr.index(min(arr))                                           # находим индексы максимального и миниммального элемента
start = min(max_i, min_i) + 1
end = max(max_i, min_i)

arry = [i for i in arr[start:end] if i < 0]
print("Начальный массив >>", arr)
print("Новый сформированный массив >>", arry)