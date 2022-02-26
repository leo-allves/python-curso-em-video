frase = 'Curso em Vídeo Python'
print(frase[:10])

# contar quantas letras "o" existe
frase = "Python"
print(frase.count('o'))
# neste caso estiver maiúsculo ele não pega para isso usamos
print(frase.upper().count('o'))
# len para ver o tamanho da frase |, mas se eu quero o tamanho menos os caracteres indesejados combinam com ‘strip’
frase = "  Python  "
print(len(frase.strip()))
# replace trocar python por Android
print(frase.replace('Python', 'Android'))
# verificar se a palavra curso esta dentro da frase
frase1 = 'Curso em Vídeo Python'
print('Curso' in frase1)  # retorna true ou false
print(frase.find('Curso'))  # ele mostra a posição o índice onde iniciou esta palavra
# caso eu busque por 'curso' em minúsculo ele não acharia para isso convertemos e buscamos com find e lower
print(frase.lower().find('curso'))
# Vou mandar escrever na tela a frase spritada com a ação de 'sprit'
frase1 = 'Curso em Vídeo Python'
print(frase1.split())  # retorno criará uma lista ['Curso', 'em', 'Vídeo', 'Python']
dividido = frase1.split()
print(dividido[0])  # mostrando a palavra que esta no índice um da lista criada pela frase
print(dividido[0][2])  # mostrando uma letra da (1.º) palavra
