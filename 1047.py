entrada = input().split()

converter = [int(numero) for numero in entrada]

h1, m1, h2, m2 = converter

if(h2 > h1):
    hf = h2 - h1
    if(m1 > m2):
        hf = hf - 1
        mf = (60 - (m1 - m2))
    elif(m1 == m2):
        mf = 0
    else:
        mf = m2 - m1
elif(h1 > h2):
    hf = 24 - (h1 - h2)
    if(m1 > m2):
        hf = hf - 1
        mf = (60 - (m1 - m2))
    elif(m1 == m2):
        mf = 0
    else:
        mf = m2 - m1
elif(h1 == h2):
    if(m1 > m2):
        hf = 23
        mf = 60 - (m1 - m2)
    elif(m1 == m2):
        hf = 24
        mf = 0
    elif(m1 < m2):
        hf = 0
        mf = m2 - m1
    
print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(hf, mf))