#imposto (PIT) PAGO UMA VEZ POR ANO

#se renda < 85.528 taloes: imposto = 18%renda - 556 taller e 2 centavos

#e a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.

#se renda > 82.528 taloes: imposoto = renda - 14.839 taloes e 2 centavos +32% do que sobra
taxa = 0
salario = float(input("Quantos foi seu salário anual?: "))

if salario < 85528:
    taxa = (salario*0.18) - 556.02
    print(f'A Taxa referente ao salário de {salario} talloes é de {round(taxa)}')
    if taxa < 0:
        print(f'A Taxa referente ao salário de {salario} talloes é de 0')
elif salario > 85528:
    taxa = ((salario - 14839.02))
    taxa = taxa - (taxa*0.32)
    print(f'A Taxa referente ao salário de {salario} talloes é de {round(taxa)}')
else:
    print("Algo deu errado.")
