opcao_tipo = int(input('\t\tQual tipo de carne deseja? (Digite o Número Correspondente)\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha\n'))

if opcao_tipo == 1:
    preco_tipo = 14.9

elif opcao_tipo == 2:
    preco_tipo = 15.9

elif opcao_tipo == 3:
    preco_tipo = 16.9

if opcao_tipo == 1 or opcao_tipo == 2 or opcao_tipo == 3:    

    quantidade = float(input('\t\tQual a quantidade de carne desejada? (kg)\n'))
    preco_tipo += 0.9 if quantidade > 5 else 0

    valor_total = preco_tipo * quantidade

    meio_pag = int(input('\t\tQual o meio de pagamento? (Digite o Número Correspondente)\n1 - Cartão do Supermercado\n2 - Outro\n'))
    valor_desc = 0.05 * valor_total if meio_pag == 1 else 0

    valor_final = valor_total - valor_desc

    print('\t\tCUPOM FISCAL\n\nTipo de Carne: ', end='')
    if opcao_tipo == 1:
        print('Filé Duplo')
    elif opcao_tipo == 2:
        print('Alcatra')
    else:
        print('Picanha')

    print('Quantidade de Carne:',quantidade,'kg')
    print('Preço Total: R$', valor_total)

    print('Tipo de Pagamento: ', end='')
    if meio_pag == 1:
        print('Cartão do Supermercado')
    else:
        print('Outro')

    print('Valor do Desconto: R$', valor_desc)
    print('Valor a Pagar: R$', valor_final)
    
else:
    print('Opção Inválida!')