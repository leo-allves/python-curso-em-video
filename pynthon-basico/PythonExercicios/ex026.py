'''
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
'''

frase = 'Ana foi viajar hoje!'
print('Aparece a letra "A" no texto {} vezes'.format(frase.upper().count('A')))
print('A letra "A" aparece na posição {} na primeira vezes.'.format(frase.upper().find('A')))
print('A letra "A" aparece na posição {} na última vezes.'.format(frase.upper().rfind('A')))


