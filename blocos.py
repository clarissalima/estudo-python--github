num1 = int(input("Digite um numero: "))

if(num1 > 10):
    print("O valor eh maior do que 10!")
    if(num1 <= 15):
        print("O valor eh maior que 10, mas menor que 15")
    elif(num1 <= 50):
        print("O valor eh maior que 10, mas menor que 50!")
    else:
        print("O valor eh maior que 50!")

elif(num1 > 5):
    print("O numero eh menor que 10 mas maior que 5!")
    if(num1 == 7):
        print("O numero eh igual a 7.")
        # so executa esse if se o elif for verdadeiro
    else:
        print("O valor eh menor que 5.")
