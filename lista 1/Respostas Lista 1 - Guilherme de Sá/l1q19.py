n = int(input('Digite o número que deseja saber a raiz quadrada: '))

a = n ** 0.5

for contador in range(1, n + 1):
    if contador < a < contador + 1:
        a = (contador + contador + 1)/2
        break
    elif a == contador or a == contador + 1:
        break

x = a ** 2 - n

if x < 0:
    x = -x


while x > 0.0001:
    a = (a - 1 + (n / (a - 1))) / 2
    x = a ** 2 - n
    
    if x < 0:
        x = -x

print('A raiz quadrada de', n,'é', a)
    