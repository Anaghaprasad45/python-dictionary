def valuesort(dic):
    k = []
    l1 = []
    for key in dic.keys():
        k.append(key)
    k = sorted(k)
    for i in k:
        l1.append(dic[i])
    print(l1)


valuesort({'x': 1, 'y': 2, 'a': 3})
