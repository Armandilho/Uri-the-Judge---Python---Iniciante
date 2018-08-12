renda = round(float(input()), 2)

impostopago = 0

valorPcalculo = renda - 2000.00

if(valorPcalculo <= 0):
    print("Isento")
else:
    #Primeiro verifica se é maior que 1000,00
    if(valorPcalculo > 1000.00):
        imposto = (1000 * 8)/100
        impostopago = impostopago + imposto
        valorPcalculo = valorPcalculo - 1000.00
        #verifica se o valor remanescente é maior que 1500,00
        if(valorPcalculo > 1500.00):
            imposto = (1500 * 18)/100
            impostopago = impostopago + imposto
            valorPcalculo = valorPcalculo - 1500.00
            #depois calcula o resto na aliquota de 28%.
            if(valorPcalculo > 0):
                imposto = (valorPcalculo * 28)/100
                impostopago = impostopago + imposto
        else:
            imposto = (valorPcalculo * 18)/100
            impostopago = impostopago + imposto
    else:
        imposto = (valorPcalculo * 8)/100
        impostopago = impostopago + imposto
        
    print("R$ {:.2f}".format(impostopago))