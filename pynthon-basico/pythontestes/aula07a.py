# OPERADORES ARITMETICOS

# (+) Adição
# (-) Subtração
# (*) Multiplicação
# (/) Divisão
# (**) Potência
# (//) Divisão INTEIRA
# (%) Resto da Divisão(Módulo)

# Calcular nota arithmetic

# Operando é o valor seja string ou numeric que será atribuido a um operador aritimetico Ex:(5+2 == )
# Seria dois operandos (5) e (2) chamamos isso de (operadores binários) para testar algo usuamos ==(igual)

# (=) Receber
# (==) Igual

5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2.5
5**2 == 25 # or pow(5,2)
5//2 == 2
5%2 == 1
81**(1/2) # Para fazer a raiz quadrada e sempre o numero pela potnecia de 1/2
127**(1/3) # Para calcular a rais cubica e sempre o valor elevado a 1/3
'OI' + 'oLÁ' == 'OIoLÁ'  # Ele vai concatenar
'Oi'*5 == 'OiOiOiOiOi' # Ele multiplica string 
'='*20 == '====================' # Muito mais eficiente rsrs e posso printar print('='*20)



# ORDEM DE PRECEDÊNCIA

# - ARITMÉTICOS 
#       ()   
#       **
#       * / // % 
#       + -  

# Ex: 
(5 + 3) * 2 == 16
5 + (3 * 2) == 11

3 * (5 + 4) ** 2 == 243
3 * 5 + 4 ** 2 == 31   
((3 * 5 + 4) ** 2) == 361

# - RELACIONAIS
#       TODOS
# - LOGICOS
#       E
#       OU
#       NÃO

#Ex: - Delimitando em quantos caractere vai aparecer na mascara {:20}
# {: 20} -> execute em vinte espaços
# {: >20} -> alinhe a direita em 20 espaços
# {: < 20} -> alinhe a esquerda em 20 espaços
# {: ^ 20} -> alinhe centralizado em 20 espaços
# {: =^ 20} -> alinhe centralizado em 20 espaços  # ===============Ana============!
# {:.3f} -> aredonda as casas 
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

# EX2: - Programa que 
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \no produto é {} e a \ndivisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão interira é {} e potência é {}'.format(di, e))

# \n quebrar a linha
# end = ' ' não quebrar