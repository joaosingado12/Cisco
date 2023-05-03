maior = int(input("Insira um numero: "))
menor = maior
i=0
while i < 5:
    numero = int(input("Insira um número: "))
    if numero> maior:
        maior = numero
    elif numero < menor:
        menor = numero
    else:
        print("")

print("O maior número digitado foi: {}\nO menor número digitado foi{}".format(maior, menor))
