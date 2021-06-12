################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 5
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero

def signo(numero):
    """
    Esta funcion indica si un valor es positivo, negativo o cero
    """
    if numero >0:
        return 'positivo'
    elif numero <0:
        return 'negativo'
    else:
        return 'cero'
    
    
def prueba():
    num = ingreso_entero('Ingrese número')
    valor =signo(num)
    print(f'el número es {valor}')
    
    
  
if __name__ == "__main__":
    prueba()
     
    
    
    