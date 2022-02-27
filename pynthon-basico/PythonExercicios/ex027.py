'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
segundo = Souza

'''

n = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Primeiro Nome: {}'.format(n[0]))
print('O último nome é: {}'.format(n[len(n)-1]))
# print('O último nome é: {}'.format(n))
# print('O último nome é: {}'.format(len(n)))
