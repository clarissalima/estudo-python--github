# exemplo 1
#a = 10
#b = 25
#c = 66

#x = int(input("Digite um número: "))

# if(x == a or x == b or x == c):
# if(x in [a, b, c]): #só precisa usar esse!
#    print("Está contido")
# else:
#    print("Não está contido")

# -------------------------------------------------------------
cores = ["azul", "amarelo", "vermelho", "branco"]

# while smp vai ser true
while True:
    cor = input("Digite uma cor ou 0 pra sair do programa: ")

    if(cor == "0"):
        break  # o programa sai do laço while
    elif cor in cores:
        print("Essa cor está contida")
    else:
        print("Essa cor não está contida")
