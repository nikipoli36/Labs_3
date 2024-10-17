import array

n = int(input("Введите размерность массива >> "))
arr = [0] * n

for i in range(len(arr)):
    arr[i] = int(input("Введите значение ячейки массива >> "))
max_i = max(arr)
print("Изначальный массив >> ", arr)
sum = 0
arry = []
for i in arr:
    if i == max_i:
        arry.append(sum)
    else:
        arry.append(i)
        sum += i
print("Преобразованный массив  >> ", arry)
