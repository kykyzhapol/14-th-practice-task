def input_number() -> int:
    '''
    Function for taking data from keyboard
    :return list:
    '''
    return int(input('Enter one number -->'))


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    d = []
    number = input_number()
    for divs in range(1, int(number ** 0.5) + 1):
        if number % divs == 0:
            d.append(divs)
    d += [number // divs for divs in d]
    print(sorted(d))


if __name__ == '__main__':
    main()
