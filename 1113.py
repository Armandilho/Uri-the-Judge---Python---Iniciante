XeY = input().split()
x, y = [int(i) for i in XeY]

while (x != y):
    if (x > y):
        print("Decrescente")
    else:
        print("Crescente")
        
    XeY = input().split()
    x, y = [int(x) for x in XeY]