#20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
#  e limitando o fatorial a números inteiros positivos e menores que 16.
n = int(input("Insira o número de vezes que deseja calcular o fatorial: "))
for i in range (1,n+1):
    while True:
        num = int(input(f'Digite o número {i}/{n} (apenas valores entre 1 e 16): '))
        if num >=1 and num <= 16: break
    fatorial = num
    for i in range (num-1,1,-1):     
        fatorial *= i
    print(f'{num}! = {fatorial}')
