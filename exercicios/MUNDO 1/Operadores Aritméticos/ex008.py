m = float(input('Digite uma distância em metros '))
k = (m/1000)
h = (m/100)
d = (m/10)
cm = (m*100)
mm = (m*1000)

print ('A medida de {} metros correspondem a\n\033[1:31m{}\033[m Quilômetros\n\033[1:31m{}\033[m Hectômetros\n\033[1:31m{}\033[m Decâmetros\n\033[1:31m{:.0f}\033[m Centímetros\n\033[1:31m{:.0f}\033[m milímetros'.format(m,k,h,d,cm,mm))
