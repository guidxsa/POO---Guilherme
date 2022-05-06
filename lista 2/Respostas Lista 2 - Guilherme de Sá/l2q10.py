def reverte_agenda(agenda, nomes, tel):
    agenda_rev = {}
    for i in range (len(agenda)):
        agenda_rev[tel[i]] = nomes[i]
    
    return agenda_rev


agenda = {}
nomes = []
tel = []
cont = 0

while True:
    nm = input('Digite o nome {} a serem adicionados: '.format(cont + 1))
    tele = input('Digite o numero {} de telefone a serem adicionados: '.format(cont + 1))

    if nm == '-1' or tele == '-1':
        break

    else:
        nomes.append(nm)
        tel.append(tele)
        cont += 1
        

for i in range (cont):
    agenda[nomes[i]] = tel[i]

agenda_rev = reverte_agenda(agenda, nomes, tel)

print('Agenda normal:\n', agenda)
print('Agenda revertida:\n', agenda_rev)