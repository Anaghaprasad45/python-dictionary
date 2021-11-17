def valuesort(dic):
    l1 = []
    k = sorted(list(dic.keys()))
    for i in k:
        l1.append(dic[i])
    print(l1)


valuesort({'x': 1, 'y': 2, 'a': 3})
