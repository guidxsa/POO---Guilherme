frase = input('Digite uma frase: ')
frase = frase.lower()

palavras = frase.split()
tam = len(palavras)

score = []



for i in range (tam):
    cont = 0
    for j in range (len(palavras[i])):
        if palavras[i][j] == 'a':
            cont += 1
        
        elif palavras[i][j] == 'e':
            cont += 1
        
        elif palavras[i][j] == 'i':
            cont += 1
        
        elif palavras[i][j] == 'o':
            cont += 1
        
        elif palavras[i][j] == 'u':
            cont += 1

    if cont % 2 == 1:
        score[i] = 2
    
    else:
        score[i] = 1

    #if (palavras[i].count('a') + palavras[i].count('e') + palavras[i].count('i') + palavras[i].count('o') + palavras[i].count('u')) % 2 == 1:
    #    score[i] = 2

    #else:
     #   score[i] = 1

media = sum(score) / len(score)

print('A pontuação média foi', media)