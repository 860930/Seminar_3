# Создайте список, состоящий из призвольных слов, 
# количество задает пользователь. Напишите программу, 
# которая определит индекс второго вхождения строки
# в списке либо сообщит, что ее нет.

from random import choices

print('Введите количество')
def create_list(k):
    words = []
    for i in range(k):
        simbol = choices('xyz', k=3)
        words.append("".join(simbol))
        return words

a = create_list(int(input()))
print(a)

def find_word(word, random_list):
    if random_list.count(word)>1:
        ind = random_list.index(word)
        return random_list.index(word, ind+1)
    else:
        return -1
print (find_word(input(),a))
