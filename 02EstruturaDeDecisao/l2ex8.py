#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = int(input("Insira o valor do primeiro produto: R$"))
prod2 = int(input("Insira o valor do segundo produto: R$"))
prod3 = int(input("Insira o valor do terceiro produto: R$"))
if prod1 < prod2 and prod1 < prod3:
    print(f'O primeiro produto deve ser comprado.')
elif prod2 < prod3:
    print(f'O segundo produto deve ser comprado.')
elif prod3 < prod2:
    print(f'O terceiro produto deve ser comprado.')
else:
    print(f'Os produtos possuem o mesmo preço.')
