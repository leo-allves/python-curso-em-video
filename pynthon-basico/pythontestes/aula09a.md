# CATEGORIAS DE FUNCIONALIDADE E SUAS FUNÇÕES

## Fatiamento

 - Em ***Paython*** uma cadeia de caractere e armazenado em um espaço

 - em uma variável porem existe dentro desta memória varias  

 - sub memorias o Python trata cada letra como um índice de 0 ...

 - Exemplo:

```python
    P y t h o n
    0 1 2 3 4 5
```

##### frase[3] 

```
Esta função identifica o caractere que esta no índice 3 neste caso o "h"
```

##### frase[1:4]

```
Esta função vou pegar o primeiro indice informado até o ultimo indice antes do ultimo informado ou seja o caracter 1 até o 3 "ytho"
```

##### frase[0:5:2]
    irá pegar o primeiro até antepenultimo de 2 em 2
    "Pto"

##### frase[:5]

    quando eu omito o idice de inicio ele começa do 0
    ou seja ficaria "Python" do 0 até o 5

##### frase[15:]

    segue mesmo raciocinio parte do indice 15 até o final 

##### frase[9::3]

    começa no 9 até o final do indice pulando de 3 em 3




## Análise

```python
C u r s o   P y t h o n
0 1 2 3 4 5 6 7 8 9 10 11
```

len = comprimento

#### len(frase)

```
função qual o comprimento da frase irá contar os micro espaços dentro da memoria neste caso 11 caracteres
```

#### frase.count('o') 

```
função conta quantas vezes aparece determinada string com a letra "o" neste caso 2 vezes
```

#### frase.count('o',0,6)

```
 além de contar ele faz um fatiamento, quantas letras "o" eu tenho do índice 0 até o 5
```

#### frase.find('Pyt')

```
  faz a contagem de quantas vezes encontrou um trecho ou caracteres sequenciais e vai de mostrar o momento que começo
```

#### frase.find('Android')

```
 Neste caso quando eu passo uma palavra ou ***string*** que não esta na ***variável, texto ou palavra*** que informei ele retornará "-1" significa que o Python varreu as strings e não achou a palavra inserida na busca
```

#### 'Curso' in frase

```
Se **existe** a palavra **curso** na frase informada 
vai retornar **True** ou **False** 
```



## Transformação

##### frase.replace('Python','Android')

```
Onde estiver a palavra **Python** ele vai substituir por **Android**
```

##### frase.upper()

```
transforma **letras** **minúsculas** em **maiúsculas**
```

##### frases.lower()

```
transforma **letras** **maiúsculas** para **minúsculas**
```

##### frase.capitalize()

```
joga **todos** os **caracteres** em **minúsculo** e só o **primeiro** em **maiúsculo**
```

##### frase.title()  
```
analisa quantas palavras em uma frase e cada primeira letra ficara maiúsculo
```

##### frase.strip()
```
strip **remove todos os espaços inúteis** do inicio e do final 
```

##### frase.rstrip()
```
**remove somente os últimos espaços** no caso da direita
```

##### frase.lstrip()
```
**remove somente os espaços no inicio**
```




## Divisão : strings 

#### frase.split()
```python
Ele vai pegar aonde **existe um espaço** de uma **palavra** a outra e fara uma **quebra** uma divisão
cada palavra recebe indexação nova e cada palavra e colocada dentro de uma outra lista.

Antes:
    
C u r s o   P y t h o n
0 1 2 3 4 5 6 7 8 9 10 11

Depois:
    
C u r s o P y t h o n
0 1 2 3 4 5 6 0 1 2 3 4 5
       1           2


​ **Retorno: ['Curso', 'Python']**   
       => Sendo 'Curso'[0] , 'Python'[1] 
```



## Junção

#### '-'.join(frase)

```
 No caso do **split** a cima onde for feita a quebra anterior se transformara com se fosse um array
​	Cada palavra se torna num novo índice em uma lista usando o join unimos com (-) (" ") da forma que desejarmos
```

Nesta função **join** estou juntando o **primeiro** grupo de caracteres criado com **segundo***
​	"Curso-Python"


[//]: # "para escrever um texto longo uso desta forma ex: abaixo"

```python
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.""")

​ O uso de aspas duplas 3X. 
```

