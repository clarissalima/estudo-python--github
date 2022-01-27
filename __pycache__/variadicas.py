def lista_de_argumentos(*lista):
  print(lista)

def lista_de_argumentos_associativos(**dicionario):
  print(dicionario)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("um", "dois", "três", "quatro")
lista_de_argumentos_associativos(a=1, b=2, c=3)