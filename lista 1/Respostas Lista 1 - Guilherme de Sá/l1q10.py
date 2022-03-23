valor_imovel = float(input('Digite o valor do imóvel:'))
salario = float(input('Digite o seu salário:'))
parcelas = int(input('Digite o número de parcelas:'))

if parcelas > 0:
    valor_mes = valor_imovel / parcelas

    if valor_mes <= 0.3 * salario:
        print('O valor da prestação é de R$', valor_mes)

    else:
        print('Financiamento não aprovado!')

else:
    print('Opção inválida!')

