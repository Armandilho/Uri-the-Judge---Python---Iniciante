valor = float(input())
valor +=  0.001
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
contador2 = 0
moeda100 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda005 = 0
moeda001 = 0


if(0 <= valor <= 1000000.00):
    
            #NOTAS#
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

        #MOEDAS#
        
    while(valor>=1): #contador de 1#
        (valor-1)
        valor= valor-1
        moeda100 = moeda100+1
    
    while(valor>=0.50): #contador de 0,50#
        (valor-1)
        valor= valor-0.50
        moeda50 = moeda50+1
        
    while(valor>=0.25): #contador de 0,25#
        (valor-1)
        valor= valor-0.25
        moeda25 = moeda25+1
        
    while(valor>=0.10): #contador de 0,10#
        (valor-1)
        valor= valor-0.10
        moeda10 = moeda10+1
        
    while(valor>=0.05): #contador de 0,05#
        (valor-1)
        valor= valor-0.05
        moeda005 = moeda005+1
    
    while(valor>=0.01): #contador de 0,01#
        (valor-1)
        valor= valor-0.01
        moeda001 = moeda001+1
    
    
        
    print("NOTAS:")
    print("%i nota(s) de R$ 100.00" %contador100)
    print("%i nota(s) de R$ 50.00" %contador50)
    print("%i nota(s) de R$ 20.00" %contador20)
    print("%i nota(s) de R$ 10.00" %contador10)
    print("%i nota(s) de R$ 5.00" %contador5)
    print("%i nota(s) de R$ 2.00" %contador2)   
    print("MOEDAS:")
    print("%i moeda(s) de R$ 1.00" %moeda100)
    print("%i moeda(s) de R$ 0.50" %moeda50)
    print("%i moeda(s) de R$ 0.25" %moeda25)
    print("%i moeda(s) de R$ 0.10" %moeda10)
    print("%i moeda(s) de R$ 0.05" %moeda005)
    print("%i moeda(s) de R$ 0.01" %moeda001)