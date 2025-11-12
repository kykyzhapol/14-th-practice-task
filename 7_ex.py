import random as rand


def chance_machine() -> list:
    exit_list = []
    for num in range(rand.randint(1, 20)):
        exit_list.append(rand.randrange(100))
    return exit_list


def count_even_odd(rand_list: list) -> None:
    odd = 0
    even = 0
    for n in rand_list:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f'sum of oss numbers = {odd}, sum of even numbers = {even}')


def main() -> None:
    count_even_odd(chance_machine())


if __name__ == '__main__':
    main()
