def penumlahan_angka(some_list, **kwargs):
    target = kwargs['target']
    for i in some_list:
        if (target - i) in some_list:
            return [i, target - i]


print(penumlahan_angka([1, 2, 3, 4, 6], target=6))
print(penumlahan_angka([2, 5, 9, 11], target=11))
