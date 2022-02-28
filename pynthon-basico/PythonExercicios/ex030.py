"""
Crie um programa que leia um número inteiro e mostre na tela se ele é "PAR" ou "ÍMPAR"

>Ideia minha pegar o número inserido se o resto da divisão(modulo) for == 0 então ele é par se não ímpar
"""

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))
