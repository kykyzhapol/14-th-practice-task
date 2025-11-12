def input_number() -> int:
    return int(input('Enter one number -->'))


def main() -> None:
    d = []
    number = input_number()
    for divs in range(1, int(number ** 0.5) + 1):
        if number % divs == 0:
            d.append(divs)
    d += [number // divs for divs in d]
    print(sorted(d))


if __name__ == '__main__':
    main()
