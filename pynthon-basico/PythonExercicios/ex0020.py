# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# sortear ordem de apresentação
#       leia o nome dos quatro alunos
#       mostra a ordem sorteada

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

# print('Sorteio: {}'.format(random.choice([a1, a2, a3, a4])))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('Ordem de apresentação: ')
print(lista)
print(random.choice(lista))


