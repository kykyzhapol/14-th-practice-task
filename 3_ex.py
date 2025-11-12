import re


def main() -> None:
    text = list(input('enter your text -->').split())
    for word in range(len(text)):
        text[word] = re.sub(r'[!-/:-@\[-`{-~]', r'', text[word])

    print(text)


if __name__ == '__main__':
    main()