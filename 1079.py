N = int(input())
i = 0

while(i < N):
    entrada = input().split()
    va1, va2, va3 = [float(num) for num in entrada]
    print("{:.1f}".format((va1*2 + va2*3 + va3*5)/10))
    i += 1