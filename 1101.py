XeY = input().split()
X, Y = [int(x) for x in XeY]
Acumulador = 0


while(X > 0 and Y > 0):
    if(X < Y):
        for i in range(X, Y + 1):
            print(X, end = ' ')
            Acumulador = Acumulador + X
            X = X + 1
        print("Sum={0}".format(Acumulador))
    else:
        for i in range(Y, X + 1):
            print(Y, end = ' ')
            Acumulador = Acumulador + Y
            Y = Y + 1
        print("Sum={0}".format(Acumulador))
    XeY = input().split()
    X, Y = [int(x) for x in XeY]
    Acumulador = 0