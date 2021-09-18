from utilidades import string_ut
from utilidades import numbers_ut
from time import sleep


def menu_():
      global menu
      string_ut.title('MENU PRINCIPAL', 0)
      for element in menu:
            for k, v in element.items():
                  print(f'{string_ut.color(3)}{k} - {string_ut.color(4)}{v}')
      print(f'{string_ut.color(0)}-' * 44)


menu = [{'1': 'Ver pessoas cadastradas'}, {'2': 'Cadastrar nova pessoa'}, {'3': 'Sair do Sistema'}]
while True:
      menu_()
      while True:
            num = numbers_ut.leiaInt(f'{string_ut.color(3)}Sua opção: ')
            if num > len(menu):
                  print(f'{string_ut.color(1)}Essa opção não existe.')
            else:
                  break
      if num == 1:
            string_ut.title(f'OPÇÃO {num}')
            sleep(1)
      elif num == 2:
            string_ut.title(f'OPÇÃO {num}')
            sleep(1)
      else:
            break
string_ut.title('Saindo do sistema... Até logo!')

