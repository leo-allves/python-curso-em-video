# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# num = random.randint(0, 10)

import random
sorteio = ('Marcos', 'Roberto', 'Manuel', 'Felipe')
print(random.sample(sorteio, k=1))
