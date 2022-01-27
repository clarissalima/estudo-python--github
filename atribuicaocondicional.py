# o programa pede ao usuario um numero e imprime se eh par ou impar
num1 = int(input("Digite um numero: "))
s = "par" if num1 % 2 == 0 else "impar"
print("O numero digitado eh", s)
