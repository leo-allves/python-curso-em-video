# Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novosalário, com 15% de aumento

salario = float(input('Digite o valor do salário R$: '))
aumento = float(input('Reajuste (%): '))
novoSalario = (salario + (salario * aumento/100))

print('Funcionário ganhava R${} \ne depois de ganhar {:.0f}% de aumento. \nSeu novo salário e de: R${:.2f}\n'.format(salario, aumento, novoSalario))
