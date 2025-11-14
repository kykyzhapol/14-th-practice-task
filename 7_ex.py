import random as rand


def chance_machine() -> list:
    '''
    Function for generate data like keyboard typing.
    :return exit_list:
    '''
    exit_list = []
    for num in range(rand.randint(1, 20)):
        exit_list.append(rand.randrange(100))
    return exit_list


def count_even_odd(rand_list: list) -> None:
    '''
    Function for counting odd and evan numbers
    :param rand_list:
    :return:
    '''
    odd = 0
    even = 0
    for n in rand_list:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f'sum of oss numbers = {odd}, sum of even numbers = {even}')


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    count_even_odd(chance_machine())


if __name__ == '__main__':
    main()
