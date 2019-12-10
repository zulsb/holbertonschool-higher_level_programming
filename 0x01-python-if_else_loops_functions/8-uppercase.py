#!/usr/bin/python3
def uppercase(str):

    for count in str:
        character = ord(count)
        if (character >= ord("a") and character <= ord("z")):
            character = character - 32
        print("{:c}".format(character), end="")
    print()
