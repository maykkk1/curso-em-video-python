from utilidades import interface
from time import sleep

while True:
      interface.menu_([{'1': 'Ver pessoas cadastradas'}, {'2': 'Cadastrar nova pessoa'}, {'3': 'Sair do Sistema'}])
      while True:
            num = interface.leiaInt(f'{interface.color(3)}Sua opção: ')
            if num > 3:
                  print(f'{interface.color(1)}Essa opção não existe.')
            else:
                  break
      if num == 1:
            interface.title(f'OPÇÃO {num}')
      elif num == 2:
            interface.title(f'OPÇÃO {num}')
      else:
            break
      sleep(1)
interface.title('Saindo do sistema... Até logo!')

