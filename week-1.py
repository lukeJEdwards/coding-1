def getInput():
    try:
        return int(input('Enter number: '))
    except:
        print('input has to be an integer.')
        return getInput()


def main():
    num = getInput()
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')


if __name__ == '__main__':
    main()
