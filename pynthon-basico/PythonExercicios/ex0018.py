# Faça um programa que leia um ângulo e mostre ma tela o valor do seno, cosseno e tangente desse ângulo.

# Os ângulos de 30º, 45º e 60º são os mais usados nos cálculos, chamados ângulos notáveis.

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo que você deseja: '))  # lendo em graus
seno = sin(radians(angulo))  # conv para radiando e calcular o seno
cosseno = cos(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo, tan))





