# Faça um programa que leia um ângulo e mostre ma tela o valor do seno, cosseno e tangente desse ângulo.

# seno = eixo vertical |   seno = cateto-oposto / hipotenusa
# cosseno = eixo horizontal --  cos = cateto-adjacente / hipotenusa
# tangente= cateto-oposto / cateto-adjacente

# Os ângulos de 30º, 45º e 60º são os mais usados nos cálculos, chamados ângulos notáveis.

import math
angulo = int(input('Digite um angulo: '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print("De acordo com o ângulo {} o seno é {:.2f} o cosseno {:.2f} e a tangente é {:.2f}.".format(angulo, seno, cosseno, tangente))





