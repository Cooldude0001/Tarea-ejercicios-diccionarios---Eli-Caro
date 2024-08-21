# Ejercicio 3
# Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario 
# con las Ilaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

def mix_diccionarios (a, b):
    mezclar = b.copy ()
    mezclar.update (a)
    print (mezclar)


diccionario1 = {'a': "  HOLA", 'b': "BIENVENIDO", 'c': "AL"}
diccionario2 = {'b': 3, 'c':20,'d': "MEZCALDOR", 'e':"DE"}
resultado = mix_diccionarios (diccionario1, diccionario2)