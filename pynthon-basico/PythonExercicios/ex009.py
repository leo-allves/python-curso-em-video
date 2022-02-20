# faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.


n1 = int(input('Digite um número: '))
print('{:=^20}'.format('TABUADA'))
print('{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {} \n{}X{} = {}'
    .format(
    (n1),(1),(n1*1), 
    (n1),(2),(n1*2),
    (n1),(3),(n1*3),
    (n1),(4),(n1*4), 
    (n1),(5),(n1*5),
    (n1),(6),(n1*6), 
    (n1),(7),(n1*7), 
    (n1),(8),(n1*8), 
    (n1),(9),(n1*9),
    (n1),(10),(n1*10)
    )
)
print('{:=^20}'.format(''))

