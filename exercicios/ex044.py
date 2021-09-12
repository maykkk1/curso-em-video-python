v = float(input('Digite o valor do produto R$: '))
print('Digite [1] para pagamento à vista dinheiro/cheque')
print('Digite [2] para pagamento à vista no cartão')
print('Digite [3] em até 2x no cartão SEM JUROS')
print('Digite [4] 3x ou mais no cartão')
p = float(input('Qual será a forma de pagamento? '))

if p == 1:
    v = v - v * 0.10
    print(f"O valor do seu produto sairá no total de R$ {'%.2f' %v}")
elif p == 2:
    v = v - v * 0.05
    print(f"O valor do seu produto sairá no total de R$ {'%.2f' %v}")
elif p == 3:
    print(f"O valor do seu produto sairá no total de R$ {'%.2f' %v}")
elif p == 4:
    v = v + v * 0.20
    print(f"O valor do seu produto sairá no total de R$ {'%.2f' %v}")
else:
    print('Opção de pagamento inválida!')