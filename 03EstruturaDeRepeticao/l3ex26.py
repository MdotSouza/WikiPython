'''26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''
n = int(input("Insira a quantidade de eleitores: "))
a = b = c = d = 0
for i in range(1,n+1):
    voto = int(input(f'''Eleitor {i}/{n}:
    Digite 1 - Primeiro Candidato
    Digite 2 - Segundo Candidato 
    Digite 3 - Terceiro Candidato
    '''))
    if voto == 1: a += 1
    elif voto == 2: b += 1
    elif voto == 3: c += 1
    else: d += 1
print(f'Votos do Candidato 1: {a}')
print(f'Votos do Candidato 2: {b}')
print(f'Votos do Candidato 3: {c}')
print(f'Votos Anulados: {d}')
