#1ts
'''
input_text = 'Enter 10 numbers through space -->'
input_list = []

while len(input_list) != 10:
    try:
        user_input = input(input_text)
        input_list = list(map(int, user_input.split()))
        if len(input_list) != 10:
            print(f'Please enter exactly 10 numbers')
    except ValueError:
        print('please, enter correct data')
        input_list = []


new_list = [input_list[0] + input_list[1]]
for n in range(2, 9):
    new_list.append(input_list[n] + input_list[n+1])

print(new_list)

from os.path import split

#2nd
input_text = 'Enter numbers through space -->'
input_list = [1.1]

while int(input_list[0]) != input_list[0]:
    try:
        user_input = input(input_text)
        input_list = list(map(int, user_input.split()))
    except ValueError:
        print('please, enter correct data')
        input_list = []

new_list = [el for el in input_list if el != 3]
print(new_list)


#3rd
import re

text = list(input('enter your text -->').split())
for word in range(len(text)):
    text[word] = re.sub(r'[!-/:-@\[-`{-~]', r'', text[word])

print(text)


#4rd
import re

text = list(input('enter your text -->').split())
for word in range(len(text)):
    text[word] = re.sub(r'[!-/:-@\[-`{-~]', r'', text[word])

print(list(set(text)))

import random as rand

import numpy


def chance_machine() -> list:
    exit_list = []
    for num in range(rand.randint(1, 20)):
        exit_list.append(rand.randrange(100))
    return exit_list

l = chance_machine()
print(l, numpy.mean(l))

#6th
d = []
number = int(input('Enter one number -->'))
for divs in range(1, int(number**0.5)+1):
    if number % divs == 0:
        d.append(divs)
d += [number//divs for divs in d]
print(sorted(d))

#8th
def sort_str(input_str: str) ->str:
    string_list = [letter for letter in input_str]
    sort_string_list = sorted(string_list)
    return str(''.join(sort_string_list))

print(sort_str('лабуба'))

#7th
import random as rand


def chance_machine() -> list:
    exit_list = []
    for num in range(rand.randint(1, 20)):
        exit_list.append(rand.randrange(100))
    return exit_list


def count_even_odd(rand_list: list) -> None:
    odd = 0
    even = 0
    for n in rand_list:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f'sum of oss numbers = {odd}, sum of even numbers = {even}')


count_even_odd(chance_machine())

import re

text_list = []
text = input('input text here. if you finished, press enter on empty string -->')
text_list += re.findall(r'\w+', text)
while text != '':
    text = input()
    text_list += re.findall(r'\w+', text)

lower_text_list = [word.lower() for word in text_list]

count_dict = {}
for item in lower_text_list:
    count_dict[item] = count_dict.get(item, 0) + 1

sorted_list = sorted(count_dict.items(), key=lambda el: el[1], reverse=True)

for word in sorted_list:
    print(word[0])

#10th
lst1 = []
while len(lst1) == 0:
    try:
        lst1 = input('enter first list thought space -->').split()
    except ValueError:
        print('please, enter minimum 1 number argument')

lst2 = []
while len(lst2) == 0:
    try:
        lst2 = input('enter second list thought space -->').split()
    except ValueError:
        print('please, enter minimum 1 number argument')


diapason = []
while len(diapason) != 2:
    try:
        diapason = [int(n) for n in input('enter 2 numbers -->').split()]
    except ValueError:
        print('please, enter two numbers')

inter_list = lst1[diapason[0]-1:diapason[1]]
del lst1[diapason[0]-1:diapason[1]]
inter_list.reverse()
lst2 += inter_list

print(lst2, lst1)


#11th
lst = []
while len(lst) == 0:
    try:
        lst = [int(n) for n in input('enter list thought space -->').split()]
    except ValueError:
        print('Please, enter elements correct')

in_command = ''
while len(in_command) == 0:
    in_command = input('Enter command Rn or Ln, where n - parameter -->')
    try:
        # Исправлена проверка команды
        if in_command[0] not in ['R', 'L'] or not in_command[1:].isdigit():
            print('Please, enter command correct')
            in_command = ''
    except IndexError:
        print('Please, enter command correct')

# Извлекаем направление и количество шагов
direction = in_command[0]
steps = int(in_command[1:])

# Выполняем сдвиг
if direction == 'R':  # Сдвиг вправо
    steps = steps % len(lst)  # Нормализуем количество шагов
    exit_lst = lst[-steps:] + lst[:-steps]
else:  # Сдвиг влево
    steps = steps % len(lst)  # Нормализуем количество шагов
    exit_lst = lst[steps:] + lst[:steps]

print(exit_lst)

#12th
dot_letters = ['a','b','d','e','g','o','p','q']

input_words = [word.lower() for word
            in input('enter words thought space and lower case -->').split()]


dot_counter = 0
normal_letter_counter = 0
dot_counter_w = 0
normal_letter_counter_w = 0
owerdoted_words = []

for word in input_words:
    dot_counter_w = 0
    normal_letter_counter_w = 0
    for letter in word:
        if letter in dot_letters:
            dot_counter_w += 1
        else:
            normal_letter_counter_w += 1
    # Убрано else и исправлено условие
    if dot_counter_w >= 2:  # Исправлено: dot_counter_w вместо dot_counter
        owerdoted_words.append(word)
    dot_counter += dot_counter_w
    normal_letter_counter += normal_letter_counter_w


print(f'dotted letters - {dot_counter}, '
      f'normal letter - {normal_letter_counter} '
      f'list of owerdoted words : {owerdoted_words}')
'''