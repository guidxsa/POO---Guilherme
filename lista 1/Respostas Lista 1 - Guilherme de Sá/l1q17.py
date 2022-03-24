n = int(input('Digite o termo que deseja ver da sequência de fibonacci: '))

termo_principal = 1
termo_anterior = 0
rodada = 1

while rodada < n:
    
    termo_principal += termo_anterior
    termo_anterior = termo_principal - termo_anterior
    
    rodada += 1

print('O valor do', n,'ésimo termo da sequência de Fibonacci é:', termo_principal)
