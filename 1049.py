filo = str(input())
classe = str(input())
alimentacao = str(input())

if(filo == "vertebrado"):
    if(classe == "ave"):
        if(alimentacao == "carnivoro"):
            print("aguia")
        else:
            print("pomba")
    elif(classe == "mamifero"):
        if(alimentacao == "onivoro"):
            print("homem")
        else:
            print("vaca")
else:
    if(classe == "inseto"):
        if(alimentacao == "hematofago"):
            print("pulga")
        else:
            print("lagarta")
    elif(classe == "anelideo"):
        if(alimentacao == "hematofago"):
            print("sanguessuga")
        else:
            print("minhoca")