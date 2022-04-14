def func(lista):
    media = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    print('Média =', media)
    print('Mínimo =', minimo)
    print('Máximo =', maximo)

lista = [1,2,3,4,5]

func(lista)
