l2 = []
d = {}


def anagram(l1):
    data = [''.join(sorted(word)) for word in l1]
    for i, e in enumerate(data):
        d.setdefault(e, []).append(i)
    for index in d.values():
        a = list(l1[i] for i in index)
        l2.append(a)
    print(l2)


anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node', 'pous'])
