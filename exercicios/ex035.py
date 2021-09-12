from colorama import Fore, Style
l1 = float(input('Digite o valor do primeiro lado '))
l2 = float(input('Digite o valor do segundo lado '))
l3 = float(input('Digite o valor do terceiro lado '))
if l1 + l2 > l3 and l3 + l1 > l2 and l2 + l3 > l1:
    print(f'{Fore.GREEN}Os segmentos acima podem formar um triângulo!{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Os segmentos acima NÃO podem formar um triângulo!{Style.RESET_ALL}')
