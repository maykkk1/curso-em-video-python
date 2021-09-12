palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for l in palavras:
    x = l.replace('', ' ').split()
    print(f'Na palavra {l} temos: ', end='')
    for y in x:
        if y in 'AEIOU':
            print(y.lower(), end=' ')
    print('')


