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
'''
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
