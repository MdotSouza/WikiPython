'''37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''
alto = baixo = somatorioAltura = gordo = magro = somatorioPeso = alunos = 0
codAlto = codBaixo = codGordo = codMagro = ""
while True:
    cod = input("Insira o código do aluno: ")
    if cod == '0':
        print(f'''
        Cliente mais alto: {codAlto} / {alto} m
        Cliente mais baixo: {codBaixo} / {baixo} m
        Cliente mais gordo: {codGordo} / {gordo} kg
        Cliente mais magro: {codMagro} / {magro} kg
        Média de altura: {somatorioAltura/alunos:.2f} m 
        Média de peso: {somatorioPeso/alunos:.2f} kg 
        ''')
        break
    else: alunos += 1
    peso = float(input("Insira o peso do aluno (kg): "))
    altura = float(input("Insira a altura do aluno (m): "))
    #verificação do peso
    if somatorioPeso == 0:
        gordo = magro = peso
        codGordo = codMagro = cod
    elif peso > gordo:
        gordo = peso
        codGordo = cod
    elif peso < magro:
        magro = peso
        codMagro = cod
    somatorioPeso += peso
    #verificação da altura
    if somatorioAltura == 0:
        alto = baixo = altura
        codAlto = codBaixo = cod
    elif altura > alto:
        alto = altura
        codAlto = cod
    elif altura < baixo:
        baixo = altura
        codBaixo = cod
    somatorioAltura += altura
