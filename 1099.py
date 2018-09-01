quantvezes = int(input())
i = 0

while(i < quantvezes):
    XeY = input().split()
    entradax, entraday = [int(x) for x in XeY]
    somadorx = 0
    somadory = 0
    if(entradax < entraday):
        if(entradax % 2 == 0):
            entradax = entradax + 1
            while(entradax < entraday):
                somadorx = somadorx + entradax
                entradax = entradax + 2
        else:
            entradax = entradax + 2
            while(entradax < entraday):
                somadorx = somadorx + entradax
                entradax = entradax + 2

    elif(entradax > entraday):
        if(entradax % 2 == 0): 
            entradax = entradax - 1
            while(entradax > entraday):
                somadorx = somadorx + entradax
                entradax = entradax - 2
        else:
            entradax = entradax -2
            while(entradax > entraday):
                somadorx = somadorx + entradax
                entradax = entradax - 2
                
    print("{0}".format(somadorx + somadory))
    i = i + 1