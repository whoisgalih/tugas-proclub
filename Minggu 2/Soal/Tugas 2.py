def merge(*args):
    temp = list()
    for arg in args:
        for i in arg:
            if i not in temp:
                temp.append(i)
    return temp


print(merge([1, 3, 5, 2, 5], [5, 3, 7, 4, 9, 5],
      [0, 9, 87, 2, 5, 9, 1, 5, 8, 23, 7]))
