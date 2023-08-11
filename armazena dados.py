##programa que armazena dados e depois mostra sei la##

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em kg: '))
maior_idade = idade >= 18

print('\n\n| Nome:', nome,'')
print('| Sobrenome:', sobrenome,'')
print('| Idade:', idade,'anos')
print('| Altura:', altura,'m')
print('| Peso:', peso,'kg')
print('| Maior de idade:',maior_idade,'\n\n')