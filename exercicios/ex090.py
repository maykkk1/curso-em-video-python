aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7:
    aluno['Situção'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}:', v)