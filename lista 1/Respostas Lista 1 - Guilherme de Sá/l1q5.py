peso = int(input('Quantos kg ele pescou? '))

multa = 0 if peso <= 50 else (peso - 50) * 5

print('Ele pescou {} kgs e pagou uma multa de R${}'.format(peso, multa))