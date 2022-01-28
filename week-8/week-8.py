import sys
import re
from string import ascii_lowercase, ascii_uppercase
from Levenshtein import distance


def binarySearch(letter):
    low, high = 0, len(dictionary) - 1
    while low < high:
        mid = (low + high) // 2
        if dictionary[mid] == letter:
            return mid
        elif dictionary[mid] < letter:
            low = mid
        else:
            high = mid
    return -1


def openFile(filename):
    with open(filename, 'r') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    file.close()
    return lines


def getNextLetter(letter):
    if letter.isupper():
        return ascii_uppercase[(ascii_uppercase.index(letter)+1) % len(ascii_uppercase)]
    else:
        return ascii_lowercase[(ascii_lowercase.index(letter)+1) % len(ascii_lowercase)]


def getWords(word, letter):
    words = []
    start_index = binarySearch(letter.lower())
    end_index = binarySearch(getNextLetter(letter.lower()))
    words += dictionary[start_index:end_index]
    start_index = binarySearch(letter.upper())
    end_index = binarySearch(getNextLetter(letter.upper()))
    words += dictionary[start_index:end_index]
    return list(filter(lambda x: len(x) == len(word), words))


def getDistances(word, dicWords):
    distances = {}
    for element in dicWords:
        d = distance(word, element)
        if d in distances:
            distances[d].append(element)
        else:
            distances[d] = [element]
    return distances


def correctWord(word):
    words = getWords(word, word[0])
    distances = getDistances(word, words)
    lowest = sorted(distances.keys())[0]
    return distances[lowest][0]


def hasNumber(word):
    return re.search('\d', word)


def correctLine(line):
    words = line.split(' ')
    new_words = []
    for word in words:
        number = hasNumber(word)
        if number != None:
            new_words.append(word)
        elif '-' in word:
            split_word = word.split('-')
            split_word[0] = correctWord(split_word[0])
            split_word[1] = correctWord(split_word[1])
            new_words.append("-".join(split_word))
        else:
            new_words.append(correctWord(word))
    return new_words


if __name__ == "__main__":
    arguemnts = sys.argv[1:]
    input_file, output_file, dictionary_file = "", "", ""

    for i, arg in enumerate(arguemnts):
        if arg == "-i":
            input_file = arguemnts[i + 1]
        if arg == "-o":
            output_file = arguemnts[i + 1]
        if arg == "-d":
            dictionary_file = arguemnts[i + 1]

    input_file_text = list(filter(None, openFile(input_file)))
    dictionary = openFile(dictionary_file)

    new_text = []
    for line in input_file_text:
        new_line = correctLine(line)
        new_text.append(" ".join(new_line))

    with open(output_file, "w") as file:
        for line in new_text:
            file.write(line + "\n" + "\n")
