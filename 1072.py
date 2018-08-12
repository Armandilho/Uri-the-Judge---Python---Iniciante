N = int(input())
i = 0
Xin = 0
Xout = 0

if(N < 10000):
    while(i < N):
        X = int(input())
        if(-10**7 < X < 10**7):
            if(10 <= X <= 20):
                Xin = Xin + 1
            else:
                Xout = Xout + 1
        i = i + 1
                
print("{0} in".format(Xin))
print("{0} out".format(Xout))