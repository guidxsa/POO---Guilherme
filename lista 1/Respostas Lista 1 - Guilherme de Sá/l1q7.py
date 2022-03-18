ganho_hora = float(input('Quanto o usuário ganha por hora? '))
horas_trab = int(input('Quantas horas o usuário trabalhou no mês? '))

sal_bruto = ganho_hora * horas_trab

IR = 0.11 * sal_bruto
INSS = 0.08 * sal_bruto
sind = 0.05 * sal_bruto

sal_liq = sal_bruto - (IR + INSS + sind)

print('\tSalário Bruto: R$', sal_bruto)
print('\tIR (11%): R$', IR)
print('\tINSS (8%): R$', INSS)
print('\tSindicato (5%): R$', sind)
print('\tSalário Líquido: R$', sal_liq)