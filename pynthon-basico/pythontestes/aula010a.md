# ESTRUTURAS DE REPETIÇÃO

### Condições Simples e Compostas

Algoritmo: 

- Um carro na estrada ao seguir haverá uma (bifurcação) y o mesmo terá 
  2 condições(caminhos) 2 possibilidades, cada caminho tem o mesmo 
  ponto de partida e o ponto final, porém um e mais rápido e outro mais longo.

- Este exemplo não significa que um e melhor que outro, mais são 2 possibilidades 
  diferentes, no dia a dia pode haver situações como uma chuva impossibilitando um caminho 
  mais existindo a possibilidade de outro para o mesmo destino.
    

````python
---------------------------------------------------
1º - Forma Didatica
---------------------------------------------------

                carro.siga()
                     ↔️
Se carro.esquerda()      SENAO
carro.siga()             carro.siga()   
carro.direita()          carro.direita()
carro.siga()             carro.siga()   
carro.direita()          carro.esquerda()
carro.esquerda()         carro.siga()
carro.siga()
carro.direita()
carro.siga()
               carro.pare() 
               
---------------------------------------------------
2º - Forma estruturada
---------------------------------------------------

carro.siga()
SE carro.esquerda()      
    carro.siga()               
    carro.esquerda()          
    carro.siga()                
    carro.direita()          
    carro.esquerda()         
    carro.siga()
    carro.direita()
    carro.siga()
SENAO
    carro.siga() 
    carro.direita() 
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()

````

- Neste exemplos podemos dizer se eu aveitar o caminho a esquerdo ele se torna "VERDADEIRO"
- E o SENAO vai ser o falso

````python
-------------------------------------
1º - Uma forma para entender
-------------------------------------
se carro.esquerda()
    bloco_V_
senão
    bloco_F_ 
-------------------------------------
2º - Como ficaria esta condição em código
-------------------------------------
if carro.esquerda()
    bloco True
else 
    bloco False
    
----------------------------------------------------------------------------
3º - Como ficaria esta condição em código usado o Input (Idade carro)
----------------------------------------------------------------------------
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
  print('Carro velho')
print('--FIM--')  

--------------------------------------------------------------------------------------
4º - Como ficaria esta condição em código usado o Input (Idade carro) em uma 3 linha
--------------------------------------------------------------------------------------

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')

````


# Condicionais Simples e Compostas

- Quando temos uma condição somente com "if", chamamos condicional simples 
- Quando temos uma condição com "if" é "else", chamamos condicional composta

````python
# Condicional Composta

nome = str(input('Qual é seu nome: '))
if nome == 'Alex':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
````



