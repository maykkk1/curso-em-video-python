from utilidades import string_ut
from time import sleep

while True:
      string_ut.menu_([{'1': 'Ver pessoas cadastradas'}, {'2': 'Cadastrar nova pessoa'}, {'3': 'Sair do Sistema'}])
      while True:
            num = string_ut.leiaInt(f'{string_ut.color(3)}Sua opção: ')
            if num > 3:
                  print(f'{string_ut.color(1)}Essa opção não existe.')
            else:
                  break
      if num == 1:
            string_ut.title(f'OPÇÃO {num}')
      elif num == 2:
            string_ut.title(f'OPÇÃO {num}')
      else:
            break
      sleep(1)
string_ut.title('Saindo do sistema... Até logo!')

