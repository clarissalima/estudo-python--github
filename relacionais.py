idade = int(input("Informe a sua idade: "))
if(idade <= 0):
    print("A sua idade nao pode ser menor ou igual a 0!")
elif(idade > 150):
    print("Pare de mentir")
elif(idade < 18):
    print("Voce eh de menor")
elif(idade >= 18):
    print("Voce eh de maior, parabens")
