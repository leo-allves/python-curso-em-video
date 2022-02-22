# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digite o valor do produto: %'))
novoPreco = preco - (preco * desconto / 100)  # regra de desconto 10*5/100 (valor)*(valor%)/(100)

print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}.\n'.format(preco, desconto, novoPreco))