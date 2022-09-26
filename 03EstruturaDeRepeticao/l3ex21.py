#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
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