# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

# Considere US$1,00 = R$3,27
real = float(input('Digite um valor R$: '))
dolar = real/3.27
print('O valor inserido foi R${} reais e você pode comprar U$${:.2f} dólareas.'.format(real, dolar))