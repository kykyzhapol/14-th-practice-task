def import_data() -> list:
    lst = []
    while len(lst) == 0:
        try:
            lst = [int(n) for n in input('enter list thought space -->').split()]
        except ValueError:
            print('Please, enter elements correct')

    in_command = ''
    while len(in_command) == 0:
        in_command = input('Enter command Rn or Ln, where n - parameter -->')
        try:
            # Исправлена проверка команды
            if in_command[0] not in ['R', 'L'] or not in_command[1:].isdigit():
                print('Please, enter command correct')
                in_command = ''
        except IndexError:
            print('Please, enter command correct')

    return [lst, in_command]


def main():
    imported_data = import_data()
    lst = imported_data[0]
    # Извлекаем направление и количество шагов
    direction = imported_data[1][0]
    steps = int(imported_data[1][1:])

    # Выполняем сдвиг
    if direction == 'R':  # Сдвиг вправо
        steps = steps % len(lst)  # Нормализуем количество шагов
        exit_lst = lst[-steps:] + lst[:-steps]
    else:  # Сдвиг влево
        steps = steps % len(lst)  # Нормализуем количество шагов
        exit_lst = lst[steps:] + lst[:steps]

    print(exit_lst)


if __name__ == '__main__':
    main()
