#!/usr/bin/python3
def fizzbuzz():

    for numeros in range(1, 101):
        if numeros % 3 == 0 and numeros % 5 == 0:
            print("FizzBuzz", end=" ")
        elif numeros % 3 == 0:
            print("Fizz", end=" ")
        elif numeros % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(numeros, end=" ")
