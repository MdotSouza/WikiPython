'''34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''
n = int(input("Insira um número: "))
primo = False
i = 2
while i < n:
    if n%i == 0:
        primo = False
        break
    else:
        primo = True
    i += 1
if primo == False: print(f'O número {n} não é primo.')
else: print(f'O número {n} é primo.')
