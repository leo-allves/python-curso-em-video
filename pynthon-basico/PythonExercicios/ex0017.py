# Teorema de Pitágoras
''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. '''

# quad da import = soma dos quadra dos catetos (a² = b² + c²)
from math import hypot

cateto_oposto = float(input('Comprimento valor do cateto oposto: '))
cateto_adjacente = float(input('Comprimento valor do cateto adjacente: '))

# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) Ou

print(f'{"":=^35}')
print("A hipotenusa do triângulo é {:.2f}".format(hypot(cateto_oposto, cateto_adjacente)))
print(f'{"":=^35}')

