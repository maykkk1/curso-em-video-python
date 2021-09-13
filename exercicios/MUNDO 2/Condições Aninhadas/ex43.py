peso = int(input('Qual o seu peso? (Kg): '))
altura = float(input('Qual a sua altura? (m): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu imc é {:.2f}. Você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.2f}. Você está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.2f}. Você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é {:.2f}. Você está com obesidade.'.format(imc))
else:
    print('Seu imc é {:.2f}. Você está com mórbida.'.format(imc))