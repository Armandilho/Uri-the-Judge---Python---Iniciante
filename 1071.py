entradax = int(input())
somadorx = 0

entraday = int(input())
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