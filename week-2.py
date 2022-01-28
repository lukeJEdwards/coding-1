def threeInts():
    try:
        # takes all three inputs and puts them into an array
        nums = [*map(int, input('Enter numbers: ').split(' '))]

        # loops through starting at nums[0] to nums[1]
        sum = 0
        for i in range(nums[0], nums[1]):
            if i % nums[2] == 0:
                sum += i
        # prints the sum of all multiples
        print(f'Sum: {sum}')
    except:
        # only printed is the inputs are not a integers
        print("Inputs have to be integers.")


def charOccurrence():
    try:
        sentence = str(input('Enter sentence: '))
        dict = {}
        # loops through the sentence character by character
        for c in sentence:
            # if the character is a space skip to the next character
            if c == ' ':
                continue
            # checks to make sure the character is part of the alphabet
            if c.isalpha():
                # checks to see if the character is part of the dictionary
                # if part of the dictionary then increaments by 1 else creates a
                # new key and set it's value to 1
                if c in dict.keys():
                    dict[c] += 1
                else:
                    dict[c] = 1
            else:
                # to make sure the sentnece doesn't contain any characters not in the alphabet.
                raise Exception("   ")

        keys = sorted(dict.keys())
        for key in keys:
            print(f'{key}: {dict[key]}')
    except:
        print("Input has to be a string.")


def division():
    try:
        # takes all three inputs and puts them into an array
        nums = [*map(int, input('Enter numbers: ').split(' '))]
        temp = nums[0]
        i = 0
        while temp >= nums[1]:
            temp -= nums[1]
            i += 1

        if temp > 0:
            print(
                f'{nums[0]} divided by {nums[1]} is {i} with a remainder of {temp}.')
        else:
            print(f'{nums[0]} divided by {nums[1]} is {i}')

    except:
        print("Inputs have to be integers.")


if __name__ == "__main__":
    division()
