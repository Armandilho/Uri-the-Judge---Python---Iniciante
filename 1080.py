i = 1
maior = 0

while(i < 101):
    entrada = int(input())
    if(entrada > maior):
        maior = entrada
        index = i
    i = i + 1

print(maior)
print(index)