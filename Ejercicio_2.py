# Ejercicio 2
# Desarrollar un algoritmo que verifique si todas las clave: valor de un diccionario se encuentran en otro diccionario.
def Verificar_key_value (diccionario1, diccionario2):
   
    for clave, valor in diccionario1.items():
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False # # Cuando las clave - valor de un diccionario NO se encuentran en otro diccionario.
    return True # Cuando las clave - valor de un diccionario se encuentran en otro diccionario.

# Ejemplos del 
diccionario1 = {'clave a': 1, 'clave b': 2,'clave c': 3}

diccionario2 = {'clave a': 1,'clave b': 2,'clave c': 3}

diccionario3 = {'clave a': 1,'clave b': 3, 'clave c': 3, 'clave d': 6}

print(Verificar_key_value (diccionario1, diccionario2)) 
print(Verificar_key_value (diccionario1, diccionario3))  
