data_in = input('Digite data: ')

mes = None

data_sep = data_in.split('/')

if data_sep[1] == '01':
    mes == 'janeiro'

elif data_sep[1] == '02':
    mes == 'fev'

elif data_sep[1] == '03':
    mes == 'mar'

elif data_sep[1] == '04':
    mes == 'abr'

elif data_sep[1] == '05':
    mes == 'mai'

elif data_sep[1] == '06':
    mes == 'jun'

elif data_sep[1] == '07':
    data_sep[1] == 'jul'

elif data_sep[1] == '08':
    data_sep[1] == 'ago'

elif data_sep[1] == '09':
    data_sep[1] == 'set'

elif data_sep[1] == '10':
    data_sep[1] == 'out'

elif data_sep[1] == '11':
    data_sep[1] == 'nov'

elif data_sep[1] == '12':
    data_sep[1] == 'dez'

msg = f'Você nasceu em {data_sep[0]} de {mes} de {data_sep[2]}'

print(msg)