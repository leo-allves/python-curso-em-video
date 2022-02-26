# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não como nome "SANTO"

city = str(input('Digite o nome de uma cidade: '))
returnCity = city.split()
print('SANTO' in returnCity[0])


