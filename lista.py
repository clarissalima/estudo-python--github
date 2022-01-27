# o codigo abaixo nao funciona
#lista_nums = [100, 200, 300, 400]
# for item in lista_nums:
#  item+=1000
# print(item)

lista_nums = [100, 200, 300, 400, 500, 600, 700, 800]
for item in range(len(lista_nums)):
    # enumerate: faz as duas coisas
    # range: gera a quantidade de itens da lista, se botasse 4
    # adicionaria 1000 aos 4 primeiros números
    # len: retorna a quantidade de numeros que a lista_nums possui
    # no caso, podemos adicionar quantos numeros quisermos que ele
    # vai adicionar automaticamente
    lista_nums[item] += 1000
# usando o for, vai adicionar 1000
# a cada elemento da lista_nums
print(lista_nums)
