older = 0
man = 0
youngWoman = 0
while True:
    print('=' * 40)
    print('\033[:1:98m          CADASTRE UMA PESSOA\033[m')
    print('=' * 40)
    age = int(input('Digite a idade: '))
    gender = ' '
    while gender not in 'FM':
        gender = str(input('SEXO [F/M]: ')).strip().upper()[0]
    if age >= 18:
        older += 1
    if gender == 'M':
        man += 1
    if gender == 'F' and age < 19:
        youngWoman += 1
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if end == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {older}')
print(f'Total de homens cadastrados: {man}')
print(f'Total de mulheres com menos de 20 anos: {youngWoman}')





