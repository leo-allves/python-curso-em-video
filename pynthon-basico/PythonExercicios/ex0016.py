# Crie um programa que leia um número "Real" qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 | O número 6.127 tem a parte Inteira 6.

import math
num = float(input('Digite um número: '))
valor = math.trunc(num)
print("O número {} tem a parte Inteira {}.".format(num, valor))
