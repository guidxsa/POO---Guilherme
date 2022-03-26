n = int(input('Digite o termo que deseja ver da sequência de fibonacci: '))

termo_principal = 1
termo_anterior = 0

for rodada in range(1, n):
    termo_principal += termo_anterior
    termo_anterior = termo_principal - termo_anterior
    
print('O valor do {}ésimo termo da sequência de Fibonacci é: {}'.format(n, termo_principal))