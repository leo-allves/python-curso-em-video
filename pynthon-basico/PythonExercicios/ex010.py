# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

# Considere US$1,00 = R$3,27
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/5.10
euro = real/5.77
print('O valor inserido foi R${:.2f} reais e você pode comprar U$${:.2f} dólareas e EUR{:.2f} euros.'.format(real, dolar, euro))