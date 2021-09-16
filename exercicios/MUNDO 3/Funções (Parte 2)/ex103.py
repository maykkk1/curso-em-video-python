def ficha(n='<desconhecido>', g=0):
    print(f'O  jogador {n} marcou {g} gol(s) no campeonato.')


def gol_check(x):
    for i in x:
        if i in '1234567890':
            return True
        else:
            return False    


#Programa principal
nome = str(input('Nome: '))
gols = str(input('Gols marcados: '))
if len(gols) == 0:
    check = False 
else:    
    check = gol_check(gols)

if nome == '' and check == False:
    ficha()
elif nome == '' and check == True:
    ficha(g=gols)    
elif len(nome) > 0 and check == False:
    ficha(n=nome)    
else:
    ficha(nome, gols)    


