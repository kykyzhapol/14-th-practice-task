def dot_letters() -> list:
    '''
    Storage with 'dotted' letters
    :return list:
    '''
    return ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']


def input_words() -> list:
    '''
    Function for correct import info from keyboard.
    :return list:
    '''
    return [word.lower() for word
            in input('enter words thought space and lower case -->').split()]


def beautiful_print(dot_counter, normal_letter_counter,
                    owerdoted_words) -> None:
    '''
    Function for beautiful printing information.
    :param dot_counter:
    :param normal_letter_counter:
    :param owerdoted_words:
    :return:
    '''
    print(f'dotted letters - {dot_counter}, '
          f'normal letter - {normal_letter_counter} '
          f'list of owerdoted words : {owerdoted_words}')


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    dot_counter = 0
    normal_letter_counter = 0
    dot_counter_w = 0
    normal_letter_counter_w = 0
    owerdoted_words = []

    for word in input_words():
        dot_counter_w = 0
        normal_letter_counter_w = 0
        for letter in word:
            if letter in dot_letters():
                dot_counter_w += 1
            else:
                normal_letter_counter_w += 1
        if dot_counter_w >= 2:
            owerdoted_words.append(word)
        dot_counter += dot_counter_w
        normal_letter_counter += normal_letter_counter_w

    beautiful_print(dot_counter, normal_letter_counter, owerdoted_words)


if __name__ == '__main__':
    main()
