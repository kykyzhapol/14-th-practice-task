def input_data() -> str:
    return input('Enter some text -->')


def sort_str(input_str: str) -> str:
    string_list = [letter for letter in input_str]
    sort_string_list = sorted(string_list)
    return str(''.join(sort_string_list))


def main() -> None:
    print(sort_str(input_data()))


if __name__ == '__main__':
    main()
