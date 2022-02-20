# faça um programa que leia a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta um área de 2m². 

litro = 2.0

largura = float(input('Digite o valor da largura: '))
altura = float(input('Digite o valor da altura: '))
area = largura * altura #area m²
tinta = area / litro

print('Uma parede com {} X {} tem uma área de {}m², será necessario {} litros de tintas'.format(largura, altura, area, tinta))