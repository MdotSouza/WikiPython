'''46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo
    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m'''
while True:
    listaSalto = []
    saltoOrdenado = []
    atleta = input("Digite o nome do atleta: ")
    if atleta == "": break
    else:
        for i in range(1,6):
            salto = float(input(f"Salto {i}/5 (em m): "))
            listaSalto.append(salto)
            saltoOrdenado.append(salto)
        saltoOrdenado.sort()
    print(f'''Atleta: {atleta}

Primeiro Salto: {listaSalto[0]:.2f} m
Segundo Salto: {listaSalto[1]:.2f} m
Terceiro Salto: {listaSalto[2]:.2f} m
Quarto Salto: {listaSalto[3]:.2f} m
Quinto Salto: {listaSalto[4]:.2f} m

Melhor salto:  {saltoOrdenado[4]:.2f} m
Pior salto: {saltoOrdenado[0]:.2f} m
Média dos demais saltos: {(saltoOrdenado[1]+saltoOrdenado[2]+saltoOrdenado[3])/3:.2f} m

Resultado final:
{atleta}: {(saltoOrdenado[1]+saltoOrdenado[2]+saltoOrdenado[3])/3:.2f} m''')
