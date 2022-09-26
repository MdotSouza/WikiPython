'''47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7
    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04'''
while True:
    listaNotas = []
    notasOrdenadas = []
    atleta = input("Digite o nome do atleta: ")
    somatorio = 0
    if atleta == "": break
    else:
        for i in range(1,8):
            salto = float(input(f"Nota {i}/7: "))
            listaNotas.append(salto)
            notasOrdenadas.append(salto)
        notasOrdenadas.sort()
    for i in range(1,6):
        somatorio += notasOrdenadas[i]
    media = somatorio/5
    print(f'''Atleta: {atleta}
Nota: {listaNotas[0]}
Nota: {listaNotas[1]}
Nota: {listaNotas[2]}
Nota: {listaNotas[3]}
Nota: {listaNotas[4]}
Nota: {listaNotas[5]}
Nota: {listaNotas[6]}

Resultado final:
Atleta: {atleta}
Melhor nota: {notasOrdenadas[6]}
Pior nota: {notasOrdenadas[0]}
Média: {media:.2f}''')
