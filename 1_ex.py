def input_data() -> list:
    '''
    Function for correct taking data from keyboard.
    :return input_list:
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
    return input_list


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    in_lst = input_data()
    new_list = [in_lst[0] + in_lst[1]]
    for n in range(2, 9):
        new_list.append(in_lst[n] + in_lst[n + 1])

    print(new_list)


if __name__ == '__main__':
    main()
