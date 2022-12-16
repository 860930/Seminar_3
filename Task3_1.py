# Создайте список из произвольных чисел, количество задает пользователь
# Напишите программу, определяющую присутствует ли в заданном списке число, 
# полученное от пользователя.
# 10
# 13

from random import sample

print('Введите число')
def zet(a, b):
    c = sample (range(1, a*2), k=a)
    print(c)
    return 'Yes' if b in c else 'No'
print(zet(int(input()), int(input())))    

