i = 0
contador = 0

while(i <= 4):
    valores = float(input())
    if(valores % 2 == 0):
        contador = contador + 1
    i = i + 1

print("{0} valores pares".format(contador))