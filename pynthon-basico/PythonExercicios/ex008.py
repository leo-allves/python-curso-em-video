# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimitros
# km hm dam m dm cm mm

metro = float(input('Digite um valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000 

print('A media de {}m corresponde a \n{}Km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(metro, km, hm, dam, dm, cm, mm))



