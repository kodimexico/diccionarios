import numpy as np

# Dos listas, uno con categorias, otro con sus valores,
# la meta es hacer un diccionario donde cada categoria tenga sus
# valores correspondientes; rojo tiene tres instancias, azul tiene dos,
# y amarillo tiene tres;
nombres = np.array(['rojo', 'azul', 'amarillo', 'rojo', 'rojo', 'azul', 'amarillo', 'amarillo'])
valores = np.array([123, 3234, 2323, 876, 435, 2341, 43562, 9898])

# Inicializar el diccionario
categorias = dict()

# Extraer uno por uno la categoria y el valor, aqui la funcion "zip" sirve
# para combinar dos valores de dos vectores en uno, y estos a su vez se asignan
# a 'x' y 'y'
for x, y in zip(nombres, valores):

    # Verificar: si la categoria (llave, key) existe, agregar el valor a su lista
    if x in categorias:
        categorias[x] += [y, ]

    # Verificar: si la categoria (llave, key) no existe, crear la categoria y agregar
    # el primer valor
    else:
        categorias[x] = [y, ]

# Imprimir el diccionario con sus categorias
print(categorias)

