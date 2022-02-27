'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    > O nome com todas as letras maiúsculas
    > O nome com todas minúsculas
    > Quantas letras ao todo (sem considerar espaços).
    > Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip  # posso acrescentar o strip diretor para tirar os espaços
print('Analisando nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu primeiro nome possui {} letras.'.format(len(nome) - nome.count(' ')))  # vai contar os espaços e retira-los

divididoNome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divididoNome[0], len(divididoNome[0])))   # Ou
# print('Seu primeiro nome tem {} letras.'.format(nome.find(''))) pega a partir do índice zero
