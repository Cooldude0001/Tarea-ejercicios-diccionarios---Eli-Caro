# Ejercicio 1
# Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
def imprimir_valores_por_tipo (diccionario):
    tipos = {type (valor) for valor in diccionario.values()}

    for tipo in tipos:
        valores_del_tipo = [valor for valor in diccionario.values() if isinstance(valor, tipo)]
        
        if valores_del_tipo:
            valores_ordenados = sorted (valores_del_tipo)
            print (f"Valores de tipo {tipo.__name__}:")
            for valor in valores_ordenados:
                print (valor)


Ejemplo = {'clave a': 15,'clave b': 12.5,'clave c': 2.0,'clave d': 4,'clave e': 'string'}

# Prueba de la funcion
imprimir_valores_por_tipo(Ejemplo)