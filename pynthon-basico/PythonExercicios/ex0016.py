# Crie um programa que leia um número "Real" qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 | O número 6.127 tem a parte Inteira 6.

'''from math import trunc
num = float(input('Digite um número: '))
valor = trunc(num)
print("O número {} tem a parte Inteira {}.".format(num, valor))'''

from math import trunc
num = float(input('Digite um número: '))
'''print('O valor digitado foi {} e sua porção inteira é {:.0f}.'.format(num, num))'''
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, int(num)))
