# Crie um algoritimo que leia um numéro e mostre o seu dobro, triplo e rais quadrada

n = int(input('Digite um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2) # ou pow(n, (1/2))

print('NÚMERO INSERIDO: {} \nDOBRO: {} \nTRIPLO: {} \nRAIZ: {:.2f}'.format(n, dobro, triplo, raiz))


