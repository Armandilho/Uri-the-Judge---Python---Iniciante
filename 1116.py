entrada = int(input())
i = 0

while(i < entrada):
    XeY = input().split()
    x, y = [int(num) for num in XeY]

    if(y == 0):
        print("divisao impossivel")
    else:
        print("{:.1f}".format(x/y))
    i = i + 1