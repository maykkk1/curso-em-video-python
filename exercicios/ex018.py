
import math
an = int (input('\033[:1:97mDigite o valor do ângulo\033[m '))
rad = math.radians(an)
print('\033[:1:97mO ângulo de\033[m \033[:4:31m{}\033[m \033[:1:97mtem o SENO de\033[m \033[:4:31m{:.2f}\033[m\n\033[:1:97m'
      'O ângulo de\033[m \033[:4:31m{}\033[m \033[:1:97mtem o COSSENO de\033[m \033[:4:31m{:.2f}\033[m\n\033[:1:97mO '
      'ângulo de\033[m \033[:4:31m{}\033[m \033[:1:97mtem a TANGENTE de\033[m \033[:4:31m{:.2f}'.format(an, math.sin(rad) ,an , math.cos(rad), an, math.tan(rad)))