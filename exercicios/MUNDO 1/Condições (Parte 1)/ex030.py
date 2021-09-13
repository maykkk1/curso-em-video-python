from colorama import Style, Fore
n = int(input(f'{Fore.LIGHTMAGENTA_EX}Digite o número {Style.RESET_ALL}'))
r = n%2
print(f'{Fore.GREEN}Este número é par'if r == 0 else f'{Fore.RED}Este número é ímpar')