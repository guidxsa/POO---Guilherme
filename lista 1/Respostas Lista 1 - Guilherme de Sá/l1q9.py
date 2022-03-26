print('Responda esse interrogatório com "sim" para as afirmativas e qualquer outra coisa para as negativas\n')

telefonou = input('\tTelefonou para a vítima? ')
esteve = input('\tEsteve no local do crime? ')
mora_perto = input('\tMora perto da vítima? ')
devia = input('\tDevia para a vítima? ')
trabalhou = input('\tJá trabalhou com a vítima? ')

sims = 0

if telefonou == 'sim':
    sims += 1

if esteve == 'sim':
    sims += 1

if mora_perto == 'sim':
    sims += 1

if devia == 'sim':
    sims += 1

if trabalhou == 'sim':
    sims += 1

if sims == 5:
    print('\nEle é um ASSASSINO!')

elif sims == 3 or sims == 4:
    print('\nEle é CÚMPLICE!')

elif sims == 2:
    print('\nEle é SUSPEITO!')

else:
    print('\nEle é INOCENTE!')
