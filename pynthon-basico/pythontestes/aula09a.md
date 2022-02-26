# CATEGORIAS DE FUNCIONALIDADE E SUAS FUNÇÕES

# Fatiamento

'''
Em Paython uma cadeia de caracter e armazenado em um espaço
em uma variável porem existe dentro desta memória varias sub memorias o Python trata cada letra como um indice de 0 ...

Ex: P y t h o n
    0 1 2 3 4 5

frase[3] 
    Esta função identifica o caracter que esta no indice 3 neste caso o "h"
frase[1:4]
    Esta função vou pegar o primeiro indice informado até o ultimo indice antes do ultimo informado ou seja o caracter 1 até o 3 "ytho"
frase[0:5:2]
    irá pegar o primeiro até antepenultimo de 2 em 2
    "Pto"
frase[:5]
    quando eu omito o idice de inicio ele começa do 0
    ou seja ficaria "Python" do 0 até o 5
frase[15:]
    segue mesmo raciocinio parte do indice 15 até o final 
frase[9::3]
    começa no 9 até o final do indice pulando de 3 em 3
'''

# Análise

'''
Ex: C u r s o   P y t h o n
    0 1 2 3 4 5 6 7 8 9 10 11

len = comprimento

len(frase)
    função qual o comprimento da frase irá contar os micro espaços dentro da memoria neste caso 11 carctres de acorsdo com ex "11"
frase.count('o')
    função conta quantas vezes aparece determinada string
    neste caso quantas vezes aparece o caracter "o" neste caso 2 vezes aparece
frase.count('o',0,6)
    alem de contar ele faz um fatiamento, quantas letras "o" eu tenho do indice 0 até o 5
frase.find('Pyt')
    faz a contagem de quantas vezes encontrou um tercho ou caracteres sequenciais e vai de mostrar o momento que começo
frase.find('Android')
    Neste caso quando eu declaro uma string que não esta na string que eu informei ele retornará -1
    significa que o Python vareu as stringues e não achou
'Curso' in frase
    Existe a palavra curso na frase informada
    vai retornar True ou False 
'''

# Transformação

'''
frase.replace('Python','Android')
    Onde estiver a palvra Python ele vai substituir por Android
frase.upper()
    transforma letras minusculos em maiusculo
frases.lower()
    transforma letras maisculo para minusculo
frase.capitalize()
    joga todas os caracteres em minusculo e so o primeiro em maisculo
frase.title()
    analisa quantas palavras em uma frase e cada primeira letra ficara maiusculo
frase.strip()
    strip remove todos os espaços inuteis do inicio e do final 
frase.rstrip()
    remove somente os ultimos espaços no caso da direita
frase.lstrip()
    remove somente os espaços no inicio
frase.spli()
'''

# Divisão

'''
### Dividir strings 

frase.split()
    Ele vai pegar aonda existe um espaço de uma palavra a outra e fara uma quebra uma divisão
    cada palavra recebe indexação nova e cada palavra e colocada dentro de uma outra lista onde cada palavra recebe um indice também ex

    ANtes: 
    Ex: C u r s o   P y t h o n
    0 1 2 3 4 5 6 7 8 9 10 11

    Depois: 
    Ex: C u r s o P y t h o n
    0 1 2 3 4 5 6 0 1 2 3 4 5
           1           2
'''

# Junção

'''
'-'.join(frase)
    No caso do split a cima onde em fiz a quebra nos espçaos
    onde me giro mais dois micro grupos ou espaços onde cada palvra tem seu indice de partida 0 ate o final da palavra
    no exemplo acima se toronaram 2 grupos

    nesta função join estou juntando o primeiro grupo de caracteres com segundo e onde acabar um havera um - tracinho ex as palavras cima ficaria

    "Curso-Python"


[//]: # (para escrever um texto longo uso desta forma ex: abaixo)


    print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
    dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen 
    book.''' O usus de aspas duplas triplas. """)



