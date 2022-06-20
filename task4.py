import random as rd

#n = int(input("Введите число чисел начиная с 1: "))
#m = int(input("Введите интервал, где концом станет первый элемент: "))
first_array = []
round_array = []

for i in range(1, n + 2):
    first_array.append(rd.i)

print()
print('Круговой массив: ')
print(*first_array, sep='')

first_array.pop()
first_array_1 = first_array * n

for j in range(len(first_array_1)):
    if(j == 0):
        round_array.append(first_array_1[j])
    elif(j % (m - 1)  == 0):
        round_array.append(first_array_1[j])
    else:
        continue       

if(round_array[int(n / 2)] == round_array[n]):
    final_array = round_array[:int(n / 2)]
else:
    final_array = round_array[:n]

print('Обход кругового массива: ')
print(*final_array, sep='')
