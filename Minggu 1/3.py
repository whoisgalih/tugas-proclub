a = '* '

b = list()

n = int(input())

for i in range(1, n+1):
    b = (a*i).split()
    print((' '.join(b)).rjust(2*n-1))