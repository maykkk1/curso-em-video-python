def fatorar(n, show=False):
    """
    -> Fatora o número digitado
    :param n: Número a ser fatorado
    :param show: (Opcional) Mostrar ou não o cálculo. 
    :return: Retorna o número fatorado
    Criado por Maycon Douglas
    """
    print('-'*30)
    f = 1
    for i in range(1, n+1):
        f *= i
    if show == True: 
        print(f'{n}!=', end=' ')
        for i in range(n, 0, -1):
            if i != 1:
                print(i, end=' x ')
            else:
                print(f'{i} = {f}.')    
        return 120
    else:
        print(f)
        return 120      


#programa principal
while True:
    num = int(input('Digite o número a ser fatorado: '))
    show_calcu = ' '
    while show_calcu not in 'SN':
        show_calcu = str(input('Deseja que o cálculo seja mostrado? [S/N] ')).upper()[0]
    if show_calcu == 'S':
        fatorar(num, show=True)
    else:
        fatorar(num)      
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja fatorar outro número? [S/N] ')).upper()[0]    
    if end == 'N':
        break      