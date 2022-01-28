def name(name, familyName=None):
    # checks to see if family name was given
    if familyName is None:
        print(f'Hello {name}.')
    else:
        print(f'Hello there, {name} of {familyName}.')


def toPigLatin(senetence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = senetence.split(' ')
    newSentence = ""
    # loops through the words in the sentence
    for word in words:
        # checks to see if the first letter of the word is a vowel
        if word[0] in vowels:
            # adds yay to the end
            newSentence += f'{word}yay '
        else:
            count = 0
            # counts the amount of constant before the first vowel and
            # moves them to the end and adds ay
            for char in word:
                if char not in vowels:
                    count += 1
                else:
                    break
            newSentence += f'{word[count:]}{word[:count]}ay '
    print(newSentence)


if __name__ == "__main__":
    toPigLatin("technique omelet string smile")
