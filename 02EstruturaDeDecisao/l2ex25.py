'''25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    - "Telefonou para a vítima?"
    - "Esteve no local do crime?"
    - "Mora perto da vítima?"
    - "Devia para a vítima?"
    - "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''
print('Responda as próximas perguntas, utilizando S para sim e N para não: ')
respostas = 0
if input("Telefonou para a vítima?: ").upper() == 'S': respostas += 1
if input("Esteve no local do crime?: ").upper() == 'S': respostas += 1
if input("Mora perto da vítima?: ").upper() == 'S': respostas += 1
if input("Devia para a vítima?: ").upper() == 'S': respostas += 1
if input("Já trabalhou com a vítima?: ").upper() == 'S': respostas += 1
if respostas == 2: print("Suspeita")
elif respostas == 3 or respostas == 4: print("Cúmplice")
elif respostas == 5: print("Assassino")
else: print("Inocente")
