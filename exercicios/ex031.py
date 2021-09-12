x = int(input('Digite a distância da viagem '))
preço = x*0.50 if x < 200 else x*0.45
print(f"O valor da sua viagem será {'%.2f' %preço}")