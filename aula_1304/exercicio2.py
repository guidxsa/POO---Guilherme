from re import A


def media(a1, a2):
    media = (a1 + a2)/2
    print('Média =', media)

x = float(input('Digite x: '))
y = float(input('Digite y: '))

media(x, y)

a = float(input('Digite a: '))
b = float(input('Digite b: '))

media(a, b)

a = a * x
b = b * y

media(a,b)