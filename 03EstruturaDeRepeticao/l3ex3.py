'''3. Faça um programa que leia e valide as seguintes informações:
    - Nome: maior que 3 caracteres;
    - Idade: entre 0 e 150;
    - Salário: maior que zero;
    - Sexo: 'f' ou 'm';
    - Estado Civil: 's', 'c', 'v', 'd';'''
while True: #validação do nome
    nome = input("Digite o nome do usuário: ")
    if len(nome) > 3:
        break
    else:
        print("Dado inválido! O nome deve ter mais que 3 caracteres.")
while True: #validação da idade
    idade = int(input("Digite a idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Dado inválido! A idade deve ser entre 0 e 150.")
while True: #validação do salário
    salario = int(input("Digite o salario: "))
    if salario > 0 :
        break
    else:
        print("Dado inválido! O salário deve ser maior que zero.")
while True: #validação do sexo
    sexo = input("Digite o sexo (f-feminino, m-masculino): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Dado inválido! Deve ser informado F ou M.")
while True: #validação do Estado Civil
    estado = input("Digite o Estado Civil (s-solteiro, c-casado, v-viúvo, d-divorciado): ").lower()
    if (estado in 'scvd') == True:
        break
    else:
        print("Dado inválido! Seleção sem opção definida.")
