#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
a = int(input("Insira a população inicial do país A: "))
iA = float(input("Insira a taxa de crescimento do país A (em %): "))
b = int(input("Insira a população inicial do país B: "))
iB = float(input("Insira a taxa de crescimento do país B (em %): "))
t = 0
while True:
    if a >= b: 
        print(f'{t} anos')
        break
    else:
        t += 1
        a += (iA/100)*t
        b += (iB/100)*t
