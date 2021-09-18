import urllib
import urllib.request
url = 'https://www.google.com.br/'
try:
    x = urllib.request.urlopen(url).getcode()
    print(f'O site {url} está funcionando normalmente.')
except Exception as erro:
    print(f'Houve algum problema. Dados do erro {erro.__class__}')

print(urllib.request.urlopen('https://www.google.com.br/').read())