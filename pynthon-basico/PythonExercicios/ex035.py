"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
> EX
r1 ________
r2 ______________
r3 _________

> Pesquisar como que e uma regra para criar um triangulo e aplicar isso em código
"""

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

# if (r1 > r2 + r3) and (r2 > r1 + r3) and (r3 > r1 + r2):

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r3 + r2 > r1):
    print('PARABÉNS! Você formou um triângulo!')
else:
    print('DESCULPE! Você não formou um triângulo!')
