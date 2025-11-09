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
'''
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
