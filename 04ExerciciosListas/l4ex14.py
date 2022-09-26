'''14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''
listaPerguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
print('Digite S (sim) ou N (não):')
cont = 0
for i in listaPerguntas:
    while True:
        x = input(f'{i}: ').upper()
        if x == "S":
            cont += 1
            break
        elif x == "N":
            break
        else: print("Seleção incorreta!")
if cont == 2: print("Suspeita")
elif cont == 3 or cont == 4: print("Cúmplice")
elif cont == 5: print("Assassino")
else: print("Inocente")
