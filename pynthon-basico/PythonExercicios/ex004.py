# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite alguma coisa: ')
print('O tipo desse valor é ', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É um alfabético?', valor.isalpha())
print('É um alfanumérico?', valor.isalnum())
print('Está em maiúsculo?', valor.isupper())
print('Está em minúsculo', valor.islower())
print('Está capitalizado', valor.istitle())

