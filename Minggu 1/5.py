a = '* '

b = list()

n = int(input())

for i in range(n, 0, -1):
    b = (a*i).split()
    print((' '.join(b)).center(2*n-1))