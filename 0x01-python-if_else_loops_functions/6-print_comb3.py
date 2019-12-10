#!/usr/bin/python3
for primer_n in range(10):
    for segundo_n in range(10):
        if primer_n < segundo_n:
            print("{:d}{:d}".format(primer_n, segundo_n), end="")
            if primer_n < 8:
                print(", ", end="")
print()
