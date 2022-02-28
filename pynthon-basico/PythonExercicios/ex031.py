"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km
e R$0,45 para viagens mais longas.
"""

km = float(input('Digite a distância em km da sua viagem: '))
print('Você está prestes a começar uma viagem de {}Km'.format(km))
preco = km * 0.50 if km <= 200 else km * 0.45
print('É o preço de sua passagem será de R${:.2f}'.format(preco))
