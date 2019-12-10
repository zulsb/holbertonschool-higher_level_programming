#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final = abs(number) % 10
if number < 0:
    final = -final
print("Last digit of {} is {} and is".format(number, final), end=" ")
if final > 5:
    print("greater than 5")
elif final == 0:
    print("{} and is 0".format(final))
else:
    print("less than 6 and not 0")
