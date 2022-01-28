nato = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "X-ray",
    "y": "Yankee",
    "z": "Zulu",
}


def toNato(string):
    newString = ""
    for char in string:
        newString += f'{nato[char]} '
    return newString


def Cipher(text, shift):
    alpha = [*nato]
    shift_alpha = alpha[shift:] + alpha[:shift]
    table = str.maketrans(''.join(alpha), ''.join(shift_alpha))
    return text.translate(table)


if __name__ == "__main__":
    print(Cipher("hello word", 7))
