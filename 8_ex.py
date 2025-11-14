def input_data() -> str:
    '''
    Function for import data from keyboard.
    :return str:
    '''
    return input('Enter some text -->')


def sort_str(input_str: str) -> str:
    '''
    Function for sorting string by letters.
    :param input_str:
    :return str:
    '''
    string_list = [letter for letter in input_str]
    sort_string_list = sorted(string_list)
    return str(''.join(sort_string_list))


def main() -> None:
    '''
    Main function, where main algorithm.
    '''
    print(sort_str(input_data()))


if __name__ == '__main__':
    main()
