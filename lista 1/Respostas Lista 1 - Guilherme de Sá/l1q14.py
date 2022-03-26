quant_consumo = float(input('Digite quantos kWh foram consumidos: '))

tipo_instal = input('Digite o tipo de instalação:\n"R" para residências, "I" para indústrias, "C" para comércios\n')

if (tipo_instal == 'R' or tipo_instal == 'I' or tipo_instal == 'C') and quant_consumo >= 0:
    if tipo_instal == 'R':
        if quant_consumo <= 500:
            preco = 0.4
    
        else:
            preco = 0.65

    elif tipo_instal == 'I':
        if quant_consumo <= 5000:
            preco = 0.55
    
        else:
            preco = 0.60

    elif tipo_instal == 'C':
        if quant_consumo <= 1000:
            preco = 0.55
    
        else:
            preco = 0.60
    
    preco_final = quant_consumo * preco

    print('O gasto total foi de R${0:.2f}'.format(preco_final))

else:
    print('Opção Inválida!')