"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
>Para salários superiores a R$1.250,00, calcule um aumento de 10%.
> Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o seu salario: '))

if salario <= 1250:
    aumento = salario + (salario / 100 * 15)
    print('Você teve um aumento de 10% e seu novo salario é R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario / 100 * 10)
    print('Você teve um aumento de 15% e seu novo salario é R${:.2f}'.format(aumento))