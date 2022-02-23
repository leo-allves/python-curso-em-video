# Adicionanando BIBLIOTECA>Modulos

# import usado para importar um modulo(pacote: biblioteca a ser carregada) no python
# para adicionar toda a biblioteca usamos 
#   importe pacote
# caso eu queira add somente 1 item do pacote eu uso
#   from nome_do_pacote import nome_item_do_pacote 
# Neste caso entendemos que existe duas maneiras de fazer importação com Python por:
#   "import" e pelo "from"

# Boblioteca padrão
# math => biblioteca matematica(já vem por padrão e funcionalidades extras)
# math=>ceil = faz um arredondamento para cima
# math=>floor = faz um arredondamento para cima
# math=>trunc = trunqueite ele vai eliminar os numeros apos a virgula
# math=>pow = Que potencia também podemos usuar 5**2
# math=> sqrt = calcular raiz quadrada
# math=>factorial = calcular o factorial

# # Add toda biblioteca de matematica
# from math import sqrt
        # import math
# # Add somente um modulo da biblioteca
        # from math import ceil
# # Quero somente o modulo de raiz quadrada
        # from math import sqrt
# # Importantando 2
        # from math import trunc, pow

# =============================================================

# PRATICA

# 1 - Calculae a raiz quadrada
# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))




