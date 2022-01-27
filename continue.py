print()
print("inicio")
i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue
    # estamos dizendo pra o programa ignorar os numeros pares e pular pro proximo ciclo
    # se tivesse um break ele nao executaria o else
    print(i)
else:
    print("else")
print("fim")
