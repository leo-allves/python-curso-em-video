# Calcular nota arithmetic

materia1 = float(input('Digite a primeira materia: '))
materia2 = float(input('Digite a segunda materia: '))
materia3 = float(input('Digite a terceira materia: '))


media = round(((materia1 + materia2 + materia3)/3), 2)


if media <= 6:
    # comment: 
    print('\nA sua média é de: {} \ninfelizmente está reprovado!' .format(media))
elif media >= 8:
    # comment: 
    print('\nA sua média é de: {} \nParabéns você está aprovado!' .format(media))

    
