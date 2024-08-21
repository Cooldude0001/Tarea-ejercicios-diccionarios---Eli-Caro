# Ejercicio 4
# Desarrollar un programa que dada una listas de personas, cada persona representada como el siguiente ejemplo: 
# {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad":101}, imprima los nombres y apellidos de las personas que están en un rango de edades.

def filtrar_por_rango_edad(personas):
    filtro = {}
    min = 15
    max = 30

    for persona in personas:
        nombre, apellido, edad = persona
        
        if min <= edad <= max:
            filtro[f"{nombre} {apellido}"] = edad

    for nombre_completo, edad in filtro.items():
        print(f"{nombre_completo}: {edad} años")

# Lista ejemplo
Nombres = [("Juan", "Mozo", 20),("Joel", "Salazar", 30),("Eli", "Caro", 22),("Santiago", "Barbosa", 35)]

filtrar_por_rango_edad (Nombres)