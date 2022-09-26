'''45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
    a. Maior e Menor Acerto;
    b. Total de Alunos que utilizaram o sistema;
    c. A Média das Notas da Turma.
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.'''
listaGabarito = []
gabarito = ""
for i in range(1,11):
    while True:
        gabarito = input(f"Informe o gabarito da questão {i}: ").upper()
        if (gabarito in 'ABCDE') == False: print("Resposta Inválida. Digite A/B/C/D/E.")
        else:
            listaGabarito += gabarito
            break
cadastroAlunos = []
maior = menor = somatorio = 0
while True:
    aluno = input("Digite seu nome (0 encerra o programa): ")
    if aluno == '0': break
    else:
        cadastroAlunos += aluno
        acertos = j = 0
        for i in listaGabarito:
            j += 1
            while True:
                resposta = input(f"Digite a resposta da questão {j}: ").upper()
                if (resposta in 'ABCDE') == False: print("Resposta Inválida. Digite A/B/C/D/E.")
                elif resposta == i:
                    acertos += 1
                    break
                else: break
            somatorio += acertos
            if acertos > maior: maior = acertos
            elif acertos < menor: menor = acertos
print(f'''Mais acertos: {maior}
Menos acertos: {menor}
Total de alunos: {len(cadastroAlunos)}
Media de notas: {(somatorio/len(cadastroAlunos)):.2f}''')