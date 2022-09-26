#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    user = input("Digite o nome do usuário: ")
    passwd = input("Digite a senha: ")
    if user != passwd:
        print("Dados Válidos!")
        break
    else:
        print("Dados inválidos! A senha deve ser diferente do nome de usuário.")