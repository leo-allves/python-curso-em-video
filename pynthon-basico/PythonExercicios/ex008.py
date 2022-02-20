# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimitros

metro = float(input('Digite um valor em metros: '))
cm = metro * 100
mm = metro * 1000 

print('A conversão de {}m é {}cm é {}mm.'.format(metro, cm, mm))


