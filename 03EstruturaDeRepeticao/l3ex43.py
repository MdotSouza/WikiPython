'''43. O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''
def verificaEntrada(produto):
    while True:
        qtd = int(input(f'Informe a quantidade de {produto}: '))
        if qtd > 0: return qtd
        else: print("A quantidade deve ser maior que ZERO.")
cod = total = qtd100 = qtd101 = qtd102 = qtd103 = qtd104 = qtd105 = 0
cupom = ['------CUPOM------']
print('''------CARDÁPIO------
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00''')
while True:
    cod = int(input('Insira um o código do item, conforme cardápio (digite 0 para encerrar): '))
    if cod == 0: break
    elif cod == 100:
        qtd100 += verificaEntrada("Cachorro Quente")
        cupom += [f'Cachorro Quente: R${1.2*qtd100:.2f}']
        total += 1.2*qtd100
    elif cod == 101:
        qtd101 += verificaEntrada("Bauru Simples")
        cupom += [f'Bauru Simples: R${1.3*qtd101:.2f}']
        total += 1.3*qtd101
    elif cod == 102:
        qtd102 += verificaEntrada("Bauru com ovo")
        cupom += [f'Bauru com ovo: R${1.5*qtd102:.2f}']
        total += 1.5*qtd102
    elif cod == 103:
        qtd103 += verificaEntrada("Hambúrguer")
        cupom += [f'Hambúrguer: R${1.2*qtd103:.2f}']
        total += 1.2*qtd103
    elif cod == 104:
        qtd104 += verificaEntrada("Cheeseburguer")
        cupom += [f'Cheeseburguer: R${1.3*qtd104:.2f}']
        total += 1.3*qtd104
    elif cod == 105:
        qtd105 += verificaEntrada("Refrigerante")
        cupom += [f'Refrigerante: R${1.3*qtd105:.2f}']
        total += 1.3*qtd105
    else: print("Opção digitida inválda!")
cupom += [f'Total: R${total:.2f}']
for i in cupom:
    print(i)
