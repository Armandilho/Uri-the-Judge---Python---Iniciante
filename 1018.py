valor = int(input())
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
contador2 = 0
contador1 = 0

print(valor)

if(0<valor<1000000):

    while(valor>=100): #contador de 100#
        (valor-100)
        valor= valor-100
        contador100 = contador100+1

    while(valor>=50): #contador de 50#
        (valor-50)
        valor= valor-50
        contador50 = contador50+1

    while(valor>=20): #contador de 20#
        (valor-20)
        valor= valor-20
        contador20 = contador20+1

    while(valor>=10): #contador de 10#
        (valor-10)
        valor= valor-10
        contador10 = contador10+1

    while(valor>=5): #contador de 5#
        (valor-5)
        valor= valor-5
        contador5 = contador5+1

    while(valor>=2): #contador de 2#
        (valor-2)
        valor= valor-2
        contador2 = contador2+1

    while(valor>=1): #contador de 1#
        (valor-1)
        valor= valor-1
        contador1 = contador1+1    

    print("%i nota(s) de R$ 100,00" %contador100)
    print("%i nota(s) de R$ 50,00" %contador50)
    print("%i nota(s) de R$ 20,00" %contador20)
    print("%i nota(s) de R$ 10,00" %contador10)
    print("%i nota(s) de R$ 5,00" %contador5)
    print("%i nota(s) de R$ 2,00" %contador2)
    print("%i nota(s) de R$ 1,00" %contador1)