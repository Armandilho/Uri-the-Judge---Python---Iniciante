i = 0
contador = 0
media = 0

while(i <= 5):
    valores = float(input())
    if(valores > 0):
        contador = contador + 1
        media = media + valores
    i = i + 1

print("{0} valores positivos".format(contador))
print("{:0.1f}".format(media/contador))