#35. Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
n = int(input("Insira um número: "))
primo = True
for j in range(2,n+1):
    i = 2
    while i < j:
        if j%i == 0:
            primo = False
            break
        else:
            primo = True
        i += 1
    if primo == True: print(j,end=" ")
