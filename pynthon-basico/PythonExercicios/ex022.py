'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas
> O nome com todas minúsculas
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome: '))
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('O nome inserido possui possui {} letras sem espaços'.format(len(nome.strip())))

dividido = nome.split()
print('O primeiro nome possui {} letras'.format(len(dividido[0])))
