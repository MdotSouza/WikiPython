'''28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                        Até 5 Kg                Acima de 5 Kg
    - File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    - Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    - Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.'''
tipo = input("Selecione o tipo de carne (F-Filé Duplo, A-Alcatra, P-Picanha): ").upper()
pag = input("Selecione a forma de pagamento (T-Cartão Tabajara, O-Outras formas): ").upper()
qtd = float(input('Insira a quantidade (em kg): '))
erro = False
valor = desconto = 0.0
txtTipo = txtPag = ""
if tipo == "F":
    txtTipo = "Filé Duplo"
    if qtd > 5: valor = qtd*5.8
    else: valor = qtd*4.9
elif tipo == "A":
    txtTipo = "Alcatra"
    if qtd > 5: valor = qtd*6.8
    else: valor = qtd*5.9
elif tipo == "P":
    txtTipo = "Picanha"
    if qtd > 5: valor = qtd*7.8
    else: valor = qtd*6.9
else:
    print("Seleção inválida")
    erro = True
if pag == "T": 
    desconto = valor*0.1
    txtPag = "Cartão Tabajara"
elif pag == "O":
    desconto = 0
    txtPag = "Outras Formas"
else:
    print("Seleção inválida")
    erro = True
if erro == False:
    print("    -"*5 + "CUPOM FiSCAL" + "-"*5)
    print(f'''
    Tipo de carne: {txtTipo}
    Quantidade (em kg): {qtd:.2f}
    Preço Total (em R$): {valor:.2f}
    Tipo de pagamento: {txtPag}
    Valor do Desconto (em R$): {desconto:.2f}
    Valor a Pagar (em R$): {valor - desconto:.2f}
    ''')
else:
    print("Erro nas entradas!")