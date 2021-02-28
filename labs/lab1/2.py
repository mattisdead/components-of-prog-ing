n = int(input('Введіть число до якого ми будемо шукати кратні числа '))

k = int(input('Введіть число, кратні якого ви хочете знайти '))
sum = 0
i = 1 
while i < n:
    if k % i == 0:
        sum = sum + i
    i = i+1 
print(sum)    