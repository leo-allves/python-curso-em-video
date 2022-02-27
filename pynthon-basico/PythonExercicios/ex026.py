'''
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
'''

# frase = 'Ana foi viajar hoje!'
frase = str(input('Digite um frase: ')).upper().strip()
print('Aparece a letra "A" no texto {} vezes'.format(frase.count('A')))
print('A letra "A" aparece na posição {} na primeira vezes.'.format(frase.find('A')+1))
# colocando de uma forma que o usuário entenda a posição a partir de 1
print('A letra "A" aparece na posição {} na última vezes.'.format(frase.rfind('A')+1))


