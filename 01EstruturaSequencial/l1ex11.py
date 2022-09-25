'''11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.'''
i1 = int(input("Insira um o primeiro número inteiro: "))
i2 = int(input("Insira um o segundo número inteiro: "))
f = float(input("Insira um número real: "))
print(f'O produto do dobro do primeiro com metade do segundo: {(i1*2)*(i2/2):.2f}')
print(f'A soma do triplo do primeiro com o terceiro: {(i1*3)+(f):.2f}')
print(f'O terceiro elevado ao cubo: {(f**3):.2f}')
