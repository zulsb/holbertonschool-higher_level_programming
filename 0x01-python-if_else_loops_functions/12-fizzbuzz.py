#!/usr/bin/python3
def fizzbuzz():
    for numeros in range(1, 101):
        if numeros % 3 == 0:
            print("Fizz", end=" ")
        elif numeros % 5 == 0:
            print("Buzz", end=" ")
        elif numeros % 15 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(numeros, end=" ")
