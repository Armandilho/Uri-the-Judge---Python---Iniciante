N = int(input())
i = 1
if(2 < N < 1000):
    while(i <= 10):
        print("{0} x {1} = {2}".format(i, N, i*N))
        i += 1