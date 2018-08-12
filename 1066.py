i = 0
contadorpar = 0
contadorimpar = 0
contadorposit = 0
contadornegat = 0

while(i <= 4):
    valores = float(input())
    if(valores % 2 == 0):
        contadorpar = contadorpar + 1
    else:
        contadorimpar = contadorimpar + 1
    if(valores > 0):
        contadorposit = contadorposit + 1
    if(valores < 0):
        contadornegat = contadornegat + 1
    i = i + 1

print("{0} valor(es) par(es)".format(contadorpar))
print("{0} valor(es) impar(es)".format(contadorimpar))
print("{0} valor(es) positivo(s)".format(contadorposit))
print("{0} valor(es) negativo(s)".format(contadornegat))