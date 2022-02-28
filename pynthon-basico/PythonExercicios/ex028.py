"""Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para usuário tentar descobrir
qual foi o número escolhido pelo computador.

 RESULTADO: O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep
computer = randint(0, 5)
# print(num)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Escolha um número: '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)  # vai esperar 2 seg

if jogador == computer:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computer, jogador))



