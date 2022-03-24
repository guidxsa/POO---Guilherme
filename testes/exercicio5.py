'''exercicio 5

b = int(input('Digite o cateto b:'))

c = int(input('Digite o cateto c:'))

a = (b**2 +  c**2)**0.5

print('A hipotenusa é:', a)'''


#exercicio 6

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura:'))

IMC = peso / altura ** 2

if IMC < 18.5 and IMC > 0:
    print('Abaixo do peso')

elif IMC >= 18.5 and IMC < 25:
    print('Saudável')

elif IMC >= 25 and IMC < 30:
    print('Peso em excesso')

elif IMC >= 30 and IMC < 35:
    print('Obesidade Grau I')

elif IMC >= 35 and IMC < 40:
    print('Obesidade Grau II (severa)')

elif IMC >= 40:
    print('Obesidade Grau II (mórbida)')

else:
    print('Voce não existe')