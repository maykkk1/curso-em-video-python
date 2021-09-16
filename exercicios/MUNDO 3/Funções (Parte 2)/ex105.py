def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos (recebe várias)
    :param sit: determina se a função mostra ou não a situação dos alunos
    :return: retorna um dicionário com os dados dos alunos
    """
    dados_notas = dict()
    dados_notas['total'] = len(n)
    dados_notas['maior'] = max(n)
    dados_notas['menor'] = min(n)
    dados_notas['média'] = sum(n)/len(n)
    if sit:
        if sum(n)/len(n) < 5:
            dados_notas['situação'] = 'RUIM'
        elif 5 < sum(n)/len(n) < 7:
            dados_notas['situação'] = 'BOM'
        else:
            dados_notas['situação'] = 'ÓTIMO'
    print(dados_notas)



#Programa principal
notas(10, 5, 7, 2, 9, 10, sit=True)

help(notas)
