N = int(input())
i = 0

if(5 < N <= 2000):
    while(i < N):
        i = i + 2
        pot = i**2
        print("{0}^2 = {1}".format(i, pot))