def invertdict(dic):
    k = []
    v = []
    for key, value in dic.items():
        k.append(key)
        v.append(value)
    d = dict(zip(v, k))
    print(d)


invertdict({'x': 1, 'y': 2, 'z': 3})
