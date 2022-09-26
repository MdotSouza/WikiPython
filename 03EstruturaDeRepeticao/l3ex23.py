'''23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''
N = int(input("Insira um número: "))
primo = True
testes = 0
for j in range(2,N+1):
    i = 2
    while i < j:
        if j%i == 0:
            primo = False
            break
        else:
            primo = True
        i += 1
        testes += 1
    if primo == True:
        print(f'Primo: {j}')
print(f'Testes necessários: {testes}')