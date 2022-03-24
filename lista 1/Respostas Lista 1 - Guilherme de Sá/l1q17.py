n = int(input('Digite o termo que deseja ver da sequência de fibonacci: '))

aux = 1
aux2 = 0
rodada = 1

while rodada < n:
    
    aux += aux2
    aux2 = aux - aux2
    
    rodada += 1

print('O valor do', n,'ésimo termo da sequência de Fibonacci é:', aux)
