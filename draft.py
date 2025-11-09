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
'''
#6th
d = []
number = int(input('Enter one number -->'))
for divs in range(int(number**0.5)+1):
    if number % divs == 0:
        d.append(divs)


