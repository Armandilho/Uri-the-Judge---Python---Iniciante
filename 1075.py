N = int(input())
i = 0
if(N < 10000):
    while(i < 10001):
        if(i % N == 2):
            print(i)
        i = i + 1