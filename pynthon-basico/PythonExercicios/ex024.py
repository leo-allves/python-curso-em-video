# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não como nome "SANTO"

city = str(input('Digite o nome de uma cidade: ')).strip().upper()
returnCity = city.split()
print('SANTO' in returnCity[0])

# Ou
# city = str(input('Digite o nome de uma cidade: ')).strip()
# print(city[:5].upper() == 'SANTO')



