'''27. Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.'''
t = int(input("Insira a quantidade de turmas: "))
somatorio = 0
for i in range(1,t+1):
    while True:
        alunos = int(input(f'Insira a quantidade de alunos da turma {i}/{t}: '))
        if alunos > 40: print("A quantidade de alunos máxima é 40")
        else: break
    somatorio += alunos
print(f'Quantidade média de alunos: {somatorio/t:.2f}')
