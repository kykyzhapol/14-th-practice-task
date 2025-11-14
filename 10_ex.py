def import_lst(number: int) -> list:
    '''
    Function for import info from keyboard correct.
    :param number:
    :return lst:
    '''
    lst = []
    while len(lst) == 0:
        try:
            lst = input(f'enter {number} list thought space -->').split()
        except ValueError:
            print('please, enter minimum 1 number argument')
    return lst


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    lst1 = import_lst(1)
    lst2 = import_lst(2)

    diapason = []
    while len(diapason) != 2:
        try:
            diapason = [int(n) for n in input('enter 2 numbers -->').split()]
        except ValueError:
            print('please, enter two numbers')

    inter_list = lst1[diapason[0] - 1:diapason[1]]
    del lst1[diapason[0] - 1:diapason[1]]
    inter_list.reverse()
    lst2 += inter_list

    print(lst2, lst1)


if __name__ == '__main__':
    main()
