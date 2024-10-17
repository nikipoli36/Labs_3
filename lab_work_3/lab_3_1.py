import array, math

arr = [0]*10
arr_y = arr
for i in range(len(arr)):
    arr[i] = int(input("Введите значение ячейки массива >> "))
print("Изначальный массив >> ", arr)

for i in range(len(arr)):
    arr_y[i] = math.log(arr[i]) / 2
    arr_y[i] = round(arr_y[i], 2)

print("Преобразованный массив >> ", arr_y)
