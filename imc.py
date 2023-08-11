##program que calcula o imc da pessoa ( nem um threat reaper calcula o da thauis carla )##

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)
print('Seu IMC é:', imc)

if imc < 18.5:
    print('Você está com magreza.')
elif imc < 25:
    print('Parabéns, seu peso está normal!')
elif imc < 30:
    print('Você está com sobrepeso. Cuidado!')
elif imc < 40:
    print('Você está obeso. Procure um especialista.')
else:
    print('Você está com obesidade grave. Procure um especialista com urgência!') 