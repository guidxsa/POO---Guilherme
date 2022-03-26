ganho_hora = float(input('Quanto o usuário ganha por hora? '))
horas_trab = int(input('Quantas horas o usuário trabalhou no mês? '))

if ganho_hora >= 0 and horas_trab >= 0:
    sal_bruto = ganho_hora * horas_trab

    IR = 0.11 * sal_bruto
    INSS = 0.08 * sal_bruto
    sind = 0.05 * sal_bruto

    sal_liq = sal_bruto - (IR + INSS + sind)

    print('\tSalário Bruto: R${0:.2f}'.format(sal_bruto))
    print('\tIR (11%): R${0:.2f}'.format(IR))
    print('\tINSS (8%): R${0:.2f}'.format(INSS))
    print('\tSindicato (5%): R${0:.2f}'.format(sind))
    print('\tSalário Líquido: R${0:.2f}'.format(sal_liq))

else:
    print('Opção inválida!')