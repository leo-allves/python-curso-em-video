# faça um programa que leia a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta um área de 2m². 

litro = 2.0

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura #area m²
tinta = area / litro

print('Uma parede tem a dimensão de {} X {} e sua área é de {:.1f}m². \nPara pintar essa parede, você precisa de {:.1f}l de tintas.'.format(largura, altura, area, tinta))