################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):
    """
    Esta función obtiene el valor del cociente y resto de dos números enteros mediante restas sucesivas
     """
    contador = int(0)
    while dividendo>=divisor:
        dividendo = dividendo - divisor
        contador = contador + 1
    return contador

def prueba():
    dividendo = ingreso_entero('Ingrese el dividendo')
    divisor = ingreso_entero('Ingrese el divisor')
    valor = division_lenta(dividendo, divisor)
    print(f' El resultado de la division es {valor}')
    

if __name__ == "__main__":
    prueba()
     
    
    
    


        
    