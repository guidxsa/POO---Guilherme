preco_produto = float(input('Digite o preço do produto: '))

if preco_produto < 0:
    preco_total = 0
    print('Opção Inválida!Digite novamente\n')

else:
    preco_total = preco_produto


while(preco_produto != 0):
    preco_produto = float(input('Digite o preço do produto: '))
    if preco_produto < 0:
        print('Opção Inválida!Digite novamente\n')
        continue

    preco_total += preco_produto

print('O preço total foi de R${0:.2f}'.format(preco_total))

while True:
    forma_pag = int(input('Digite a forma de pagamento:\n1 - À vista\n2 - Cartão de Crédito\n'))

    if forma_pag == 1:
        preco_total -= 0.15 * preco_total

    elif forma_pag == 2:
        preco_total /= 4
    else:
        print('Opção Inválida! Tente novamente\n')
        continue
    print('O valor cobrado foi de R${0:.2f}'.format(preco_total))
    break