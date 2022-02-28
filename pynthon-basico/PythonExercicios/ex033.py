"""
Faça um programa que leia três números
e mostre qual é o "MAIOR" é qual é o "MENOR";
"""

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

"""
if n1 > n2 and n1 > n3:
    print('O número maior é {}'.format(n1))
elif n1 < n2 and n1 < n3:
    print('O número menor é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O número maior é {}'.format(n2))
elif n2 < n1 and n2 < n3:
    print('O número menor é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número maior é {}'.format(n3))
elif n3 < n1 and n3 < n2:
    print('O número menor é {}'.format(n3))
    
    OU
"""

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))