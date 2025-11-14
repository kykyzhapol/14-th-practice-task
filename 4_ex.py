import re


def main() -> None:
    '''
    Main function, where main algorithm.
    :return:
    '''
    text = list(input('enter your text -->').split())
    for word in range(len(text)):
        text[word] = re.sub(r'[!-/:-@\[-`{-~]', r'', text[word])

    print(list(set(text)))


if __name__ == '__main__':
    main()
