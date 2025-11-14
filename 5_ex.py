import random as rand
import numpy


def chance_machine() -> list:
    '''
    Function for generate list number from keyboard.
    :return exit_list:
    '''
    exit_list = []
    for num in range(rand.randint(1, 20)):
        exit_list.append(rand.randrange(100))
    return exit_list


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    l = chance_machine()
    print(l, numpy.mean(l))


if __name__ == '__main__':
    main()
