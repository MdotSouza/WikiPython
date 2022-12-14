'''36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''
n = int(input("Montar a tabuada de: "))
start = int(input("Começar por: "))
while True:
    end = int(input("Terminar em: "))
    if end < start: print("O valor final não pode ser menor que o de começo!")
    else: break
for i in range(start,end+1):
    if i == start: print(f'''Vou montar a tabuada de {n} começando em {start} e terminando em {end}:
{n} X {i} = {n*i}''')
    else: print(f'{n} X {i} = {n*i}')
