l = float(input('\033[:1:97mDigite a largura da parede\033[m '))
a = float(input('\033[:1:97mDigite a altura da parede\033[m '))
ar = l*a
t = ar/2
print('\033[37mSua parede tem a dimensão de\033[m \033[30m{}x{}\033[m '
      '\033[37me sua área é de\033[m \033[30m{}m²\033[m\n\033[37mPara pintar a parede, você precisará de\033[m \033[30m{:.2f}l\033[m \033[37mde tinta\033[m'.format(l,a,ar,t))