distancia = float(input('Digite quantos km deseja percorrer: '))

if distancia >= 0:

    taxa = 0.5 if distancia <= 200 else 0.45

    preco_passagem = distancia * taxa

    print('A passagem custou R$', preco_passagem)

else:
    print('Valor inválido!')