a = '* '

b = list()

for i in range(int(input()), 0, -1):
    b = (a*i).split()
    print(' '.join(b))