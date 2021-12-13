def minAppear(some_list):
    x = list(int(i) for i in some_list)
    y = dict.fromkeys(set(x), 0)

    for i in x:
        y[i] += 1

    key = list(k for k, v in y.items() if v == 1)
    return key


print(minAppear(input()))
