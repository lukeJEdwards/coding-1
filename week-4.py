from functools import reduce


def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def mult(a, b):
    print(a, b)
    if isNumber(a) and isNumber(b):
        a = float(a)
        b = float(b)
        return a * b
    else:
        return a


def multiplyNums(numArray):
    return reduce(mult, numArray, 1)


def combos(array, includeSelf=False):
    newList = []
    for item1 in array:
        for item2 in array:
            if includeSelf:
                newList.append(f'{item1} {item2}')
            else:
                if item1 == item2:
                    continue
                else:
                    newList.append(f'{item1} {item2}')
    return newList


if __name__ == "__main__":
    print(combos(["comfortable", "round", "support", "machinery"]))
