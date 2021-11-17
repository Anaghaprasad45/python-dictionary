def read_words(filename):
    return open(filename).read().split()


def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


def main(filename):
    frequency = word_frequency(read_words(filename))
    a = dict(sorted(frequency.items(), reverse=True, key=lambda x: x[1]))
    for k, v in a.items():
        print(k, v)


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
