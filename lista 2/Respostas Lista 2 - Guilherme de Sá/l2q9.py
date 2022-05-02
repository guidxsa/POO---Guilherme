def eh_palindroma(string):
    string = string.lower()

    tam = len(string)

    for i in range (tam - 1):
        if(string[i] == string[tam - 1 - i]):
            continue
        else:
            return False

    return True


string = input('Digite uma palavra:')

resultado = eh_palindroma(string)

print('A palavra é palíndroma?', resultado)