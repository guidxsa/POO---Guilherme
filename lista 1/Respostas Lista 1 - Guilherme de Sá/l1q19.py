n = int(input('Digite o número que deseja saber a raiz quadrada: '))

a = n ** 0.5

for contador in range(1, n + 1):
    if contador < a < contador + 1:
        a = contador + 0.5
        break
    elif a == contador:
        break

x = a ** 2 - n

if x < 0:
    x = -x


while x > 0.0001:
    a = (a + (n / a)) / 2
    x = a ** 2 - n
    
    if x < 0:
        x = -x

print('A raiz quadrada de {} é {}'.format(n, a))