##programa que le 2 numeros e mostra o maior (ja fiz isso em umas 5 linguagems diferentes)##

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(num1, 'é maior do que', num2)
elif num2 > num1:
    print(num2, 'é maior do que', num1)
else:
    print('Os números tem o mesmo valor ou são iguais')