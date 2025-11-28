import copy


m = 3
n = 3
lista_n_elementos = []
lista_n_listas = []

for i in range(n):
    lista_n_elementos.append('.') # A matriz é populada com pontos

for y in range(m):
    lista_n_listas.append(lista_n_elementos)
    lista_n_listas = copy.deepcopy(lista_n_listas)

lista_n_listas[0][0] = 'p'
print(lista_n_listas)



