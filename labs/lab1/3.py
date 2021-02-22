from random import seed
from random import randint

n = int(input('Enter size of an array: '))
a = [0] * n

seed (1)
for i in range(n):
    a[i] = randint(-50, 50)
    i = i+1
print(a)

i = 0
max = a[0]
numb = 0
sumofneg = 0
while i < len(a):
    if a[i] > max:
        max = a[i]
    if a[i] < 0:
        numb = numb + 1
        sumofneg = sumofneg + a[i]
    i = i+1    

if numb != 0:
    mid = sumofneg / numb
    print('The average of all negative numbers is', mid)
else:
    print('There are no negative numbers')
print('The maximum is', max) 

i = len(a) - 1
while i >= 0:
    if a[i] > 0:
        print(a[i], end =" ")
    i = i - 1