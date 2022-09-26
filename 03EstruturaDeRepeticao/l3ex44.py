'''44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são: 1 , 2, 3, 4  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco
    Faça um programa que calcule e mostre:
    - O total de votos para cada candidato;
    - O total de votos nulos;
    - O total de votos em branco;
    - A percentagem de votos nulos sobre o total de votos;
    - A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''
print('''------CANDIDATOS------
1 - JOSÉ
2 - JOÃO
3 - JACKSON
4 - JORGE
5 - VOTO NULO
6 - VOTO EM BRANCO''')
voto1 = voto2 = voto3 = voto4 = voto5 = voto6 = total = 0
while True:
    cod = int(input('Insira um o código do candidato (digite 0 para encerrar): '))
    if cod == 0: break
    elif cod == 1:
        voto1 += 1
        total += 1
    elif cod == 2:
        voto2 += 1
        total += 1
    elif cod == 3:
        voto3 += 1
        total += 1
    elif cod == 4:
        voto4 += 1
        total += 1
    elif cod == 5:
        voto5 += 1
        total += 1
    elif cod == 6:
        voto6 += 1
        total += 1
    else: print("Opção digitida inválda!")
print(f'''Votos para o candidato 1 - JOSÉ: {voto1}
Votos para o candidato 2 - JOÃO: {voto2}
Votos para o candidato 3 - JACKSON: {voto3}
Votos para o candidato 4 - JORGE: {voto4}
Total de votos nulos: {voto5}
Total de votos em branco: {voto6}
Porcentagem de votos nulos: {(voto5/total)*100:.2f}%
Porcentagem de votos brancos: {(voto6/total)*100:.2f}%''')
