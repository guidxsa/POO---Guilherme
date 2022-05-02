opcoes = (1, 2, 3, 4, 5)
lista = []

escolha = 1
while escolha in opcoes:
    escolha = int(input('\t\tQuestionário\n\nDigite sua avaliação sobre a qualidade da comida do refeitório do Ifes, de 1 (PÉSSIMO) - 5 (EXCELENTE): '))
    lista.append(escolha)  

lista.pop()
lista.sort()
minimo = min(lista)
maximo = max(lista)
media = sum(lista)/len(lista)
mediana = lista[len(lista)//2] if len(lista) % 2 == 1 else (lista[len(lista)//2] + lista[len(lista)//2 + 1])/2

lista_modal = [lista.count(1), lista.count(2), lista.count(3), lista.count(4), lista.count(5)]

for i in range (5):
    if lista_modal[i] == max(lista_modal):
        moda = i + 1
    

for j in range(len(lista)):
    var = (lista[i] - media)**2

variancia = var/len(lista)

desvio =  variancia ** (1/2)


print('A avaliação mínima foi:', minimo)
print('A avaliação máxima foi:', maximo)
print('A avaliação média foi:', media)
print('A mediana foi:', mediana)
print('A moda foi:', moda)
print('A variância foi:', variancia)
print('O desvio padrão foi:', desvio)
