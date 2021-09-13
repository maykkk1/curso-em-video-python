n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))

if (n1 + n2)/2 < 5.0:
    print(f'A média do aluno é {(n1 + n2)/2} e ele está REPROVADO.')
elif 5.0 <= (n1 + n2)/2 < 7:
    print(f'A média do aluno é {(n1 + n2)/2} e ele está em RECUPERAÇÃO.')
else:
    print(f'A média do aluno é {(n1 + n2)/2} e ele está APROVADO.')