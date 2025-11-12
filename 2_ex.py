def input_data() -> list:
    '''
    function for import data from consol
    :return:
    '''
    input_text = 'Enter numbers through space -->'
    input_list = [1.1]

    while int(input_list[0]) != input_list[0]:
        try:
            user_input = input(input_text)
            input_list = list(map(int, user_input.split()))
        except ValueError:
            print('please, enter correct data')
            input_list = []
    return input_list


def main() -> None:
    '''
    main function
    :return:
    '''
    new_list = [el for el in input_data() if el != 3]
    print(new_list)


if __name__ == '__main__':
    main()
