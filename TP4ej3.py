################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrenheit(centigrado):
    """
    Esta funcion convierte grados centígrados a fahrenheit
    """
    return ((centigrado *9/5) + 32)

def convertir_a_centigrado(fahrenheit):
    """
    Esta funcion convierte grados fahrenheit a centígrado
    """
    return ((fahrenheit - 32)*5/9)

def prueba():
    centi = float(input('Ingrese grados centígrados a convertir '))
    valor = convertir_a_fahrenheit(centi)
    print (f'El resultado es {valor}')
    
def prueba2():
    fahren = float(input('Ingrese grados fahrenheit a convertir '))
    valor = convertir_a_centigrado(fahren)
    print (f'El resultado es {valor}')

if __name__ == "__main__":
    prueba2()
    
    
    