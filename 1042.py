lista = input().split()

variavel = [int(num) for num in lista]

for elemento in sorted(variavel):
    print(elemento)

print("")

for elemento in lista:
    print(elemento)