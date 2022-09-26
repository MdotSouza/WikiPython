#22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
n = int(input("Insira um número: "))
primo = False
i = 2
while i < n:
    if n%i == 0:
        primo = False
        break
    else:
        primo = True
    i += 1
if primo == False: 
    print(f'Os diviores do número {n} são: ')
    i = 1
    while i <= n:
        if n%i == 0:
            print(i,end=" ")
        i += 1
else:
    print(f'O número {n} é primo.')