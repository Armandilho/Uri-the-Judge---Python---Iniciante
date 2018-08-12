entrada = int(input())
i = 0

if(entrada % 2 == 0):
    entrada = entrada + 1
while(i <= 5):
    print(entrada)
    entrada = entrada + 2
    i = i + 1