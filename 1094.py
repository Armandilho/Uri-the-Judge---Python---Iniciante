N = int(input())
i = 0
total = 0
contadorC = 0
contadorR = 0
contadorS = 0
while(i < N):
    Qtd, tipo = input().split()
    Qtd = int(Qtd)
    total += Qtd
    if(1 <= Qtd <= 15):
        if(tipo == 'C'):
            contadorC += Qtd
        elif(tipo == 'R'):
            contadorR += Qtd
        elif(tipo == 'S'):
            contadorS += Qtd
    
    i += 1

print("Total: {0} cobaias".format(total))
print("Total de coelhos: {0}".format(contadorC))
print("Total de ratos: {0}".format(contadorR))
print("Total de sapos: {0}".format(contadorS))
print("Percentual de coelhos: {:.2f} %".format((contadorC/total)*100))
print("Percentual de ratos: {:.2f} %".format((contadorR/total)*100))
print("Percentual de sapos: {:.2f} %".format((contadorS/total)*100))