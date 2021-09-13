from colorama import Style, Fore
v = int(input('Qual é a velocidade atual do seu carro? '))
if v > 80:
    print(f"{Fore.RED}Cuidado, você está dirigindo com excesso de velocidade!{Style.RESET_ALL} {Fore.YELLOW}Você terá que pagar"
          f" uma multa no valor de R$ {'%.2f' % ((v-80)*7.00)}")
print('Tenha um bom dia! Dirija com segurança.')
