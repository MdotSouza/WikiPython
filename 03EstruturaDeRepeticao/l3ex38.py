'''38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''
salario = float(input("Informe o salário inicial: "))
taxa = 6/100
for i in range(1998,2022):
    taxa *= 2
print(f'Salário atual: {salario*taxa:.2f}')
