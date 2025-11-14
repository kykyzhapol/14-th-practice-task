import re


def import_text() -> list:
    '''
    Function for import info from keyboard correctly.
    :return text_list:
    '''
    text_list = []
    text = input('input text here. '
                 'if you finished, press enter on empty string -->')
    text_list += re.findall(r'\w+', text)
    while text != '':
        text = input()
        text_list += re.findall(r'\w+', text)
    return text_list


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    lower_text_list = [word.lower() for word in import_text()]

    count_dict = {}
    for item in lower_text_list:
        count_dict[item] = count_dict.get(item, 0) + 1

    sorted_list = sorted(count_dict.items(), key=lambda el: el[1],
                         reverse=True)

    for word in sorted_list:
        print(word[0])


if __name__ == '__main__':
    main()
