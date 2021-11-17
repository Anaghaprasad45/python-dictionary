import sys


def character_frequency(f):
    frequency = {}
    for c in f:
        frequency[c] = frequency.get(c, 0) + 1
    print(frequency)
    a = f.split(".")
    if a[1] == 'txt':
        print("Text file")
    if a[1] == "py":
        print("Python file")
    if a[1] == "c":
        print("C program file")


file = sys.argv[1]

character_frequency(file)
