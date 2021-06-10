################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero(mensaje):
    """
    Esta función muestra un mensaje y agrega # para indicar el ingreso de un número entero.
    """
    ingreso = input(mensaje + "  #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("no es un número entero") from err        
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta función muestra un mensaje cuando se ingresa un valor erróneo e indica la cantidad de intentos disponibles.
    """
    while cantidad_reintentos > 0:
        try:
            valor = ingreso_entero(mensaje)
            return valor
        except IngresoIncorrecto as error:
            cantidad_reintentos = cantidad_reintentos -1
            print(f'Te quedan {cantidad_reintentos}')
    raise IngresoIncorrecto("Te quedaste sin intentos")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    """
    Esta función restringe el valor del número a ingresar para que sea un valor entre 0 y 10.
    """
    while ingreso_entero:
        try:
            valor = ingreso_entero(mensaje) 
            return valor
        except IngresoIncorrecto as err:
            valor_minimo =0
            valor_maximo = 10
            print(f' valor fuera de rango, volver a ingresar nuevo número')
        raise IngresoIncorrecto("valor correcto")
    
    

def prueba():
    print (f' Ingreso valor entero')
    valor = ingreso_entero_restringido('Ingrese un número entero')
    print(f'El valor ingresado fue {valor}')

if __name__ == "__main__":
     prueba()