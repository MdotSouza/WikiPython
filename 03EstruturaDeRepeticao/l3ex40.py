'''40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
    a. Código da cidade;
    b. Número de veículos de passeio (em 1999);
    c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    - Qual a média de veículos nas cinco cidades juntas;
    - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''
maisAcidentes = menosAcidentes = codMaisAcid = codMenosAcid = somaVeiculos = somaAcidentes = nAcidentes = 0
for i in range(1,6):
    cod = int(input(f"Insira o código da cidade {i}/5: "))
    veiculos = int(input("Insira o número de veículos de passeio (em 1999): "))
    acidentes = int(input("Insira o número de acidentes de trânsito com vítimas (em 1999): "))
    #verifica quantidade de acidentes
    if i == 1:
        maisAcidentes = menosAcidentes = acidentes
        codMaisAcid = codMenosAcid = cod
    elif acidentes > maisAcidentes:
        maisAcidentes = acidentes
        codMaisAcid = cod
    elif acidentes < menosAcidentes:
        menosAcidentes = acidentes
        codMenosAcid = cod
    #media de veículos
    somaVeiculos += veiculos
    #acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
    if veiculos < 2000:
        somaAcidentes += acidentes
        nAcidentes += 1
print(f'CIDADE COM MAIOR ÍNDICE DE ACIDENTES: {codMaisAcid} / {maisAcidentes}')
print(f'CIDADE COM MENOR ÍNDICE DE ACIDENTES: {codMenosAcid} / {menosAcidentes}')
print(f'MÉDIA DE VEÍCULOS: {somaVeiculos/5:.2f}')
print(f'MÉDIA DE ACIDENTES (EM CIDADES COM MENOS DE 200 VEÍCULOS): {somaAcidentes/nAcidentes:.2f}')