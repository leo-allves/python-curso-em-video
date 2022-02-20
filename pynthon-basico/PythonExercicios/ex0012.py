# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do produto: '))
novoPreco = (preco - (preco/100)*desconto)

print('Com {}% de desconto, o produto sai por {}\n'.format(desconto, novoPreco))