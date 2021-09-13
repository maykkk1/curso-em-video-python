alunos = [['No', 'Aluno', 'Média']]
aluno = list()
notas = list()
nota = list()
index = 0
while True:
    nome = str(input('Nome: ')).strip().capitalize().split()[0]
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(index)
    aluno.append(nome)
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    index += 1
    nota.append(nota1)
    nota.append(nota2)
    notas.append(nota[:])
    nota.clear()
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja adicionar mais algum aluno? ')).strip().upper()
    if end == 'N':
        break

print('-='*19)
for pos, aluno in enumerate(alunos):
    if pos == 1:
        print('='*21)
    for pos, elemento in enumerate(aluno):
        if pos == 0:
            print('{:<5}'.format(elemento), end='')
        elif pos == 1:
            print('{:<10}'.format(elemento), end='')
        elif pos == 2:
            print('{:<5}'.format(elemento), end='')
    print('')

while True:
    index_alunos = int(input('Mostrar notas de qual aluno? [999 INTERROMPE] '))
    if index_alunos == 999:
        break
    print(f'As notas do aluno {alunos[index_alunos + 1][1]} são {notas[index_alunos]}')

print('Programa finalizado!')