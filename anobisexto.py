"""se o número do ano não é divisível por quatro, é um ano comum;
caso contrário, se o número do ano não for divisível por 100, será um ano bissexto;
caso contrário, se o número do ano não for divisível por 400, é um ano comum ;
caso contrário, é um ano bissexto """

ano = int(input("Insira um Ano: "))

if ano % 4 !=0 and ano % 100 != 0:
    print(f"{ano} é um ano comum")
elif ano % 4 == 0 or ano % 400 ==0:
    print(f'{ano} É um ano bissexto')