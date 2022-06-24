from l4q10 import Ingresso, IngressoVIP

if __name__ == '__main__':
    valor = float(input('Digite o preço do Ingresso: '))
    ingresso = Ingresso(valor)

    acrescimo = 0.5 * ingresso.valor

    ingresso_vip = IngressoVIP(valor, acrescimo)

    ingresso_vip.set_calcula_VIP()

    ingresso.imprimir_valor()

    print('\nO preço do Ingresso VIP é: R${:.2f}'.format(ingresso_vip.get_calcula_VIP()))

    diferenca = ingresso_vip.get_calcula_VIP() - ingresso.valor

    print('\nA diferença de preços é de: R${:.2f}'.format(diferenca))
