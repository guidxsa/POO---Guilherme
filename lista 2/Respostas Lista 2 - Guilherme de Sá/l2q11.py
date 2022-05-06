string = input('Digite uma string: ')
tam = len(string)
lista = []
lista_final = []

for i in range (tam):
    num = ord(string[i])
    lista.append(num)

for i in range (tam):
    if lista[i] % 2 == 1:
        lista[i] += 1
    else:
        lista[i] -= 1

for i in range (tam):
    letra = chr(lista[i])
    lista_final.append(letra)
    
texto = ''

for i in range (tam):
    texto += lista_final[i]

print(texto)