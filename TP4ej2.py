################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero

def suma_lenta(numero, otro_numero):
    """
    Realiza la suma de dos números en forma indirecta
    """
    return numero + otro_numero

def prueba():
    print('Suma lenta de dos números')
    num = ingreso_entero('Primer número')
    num2 = ingreso_entero('Segundo número')
    resultado = suma_lenta(num,num2)
    print(f'El resultado de la suma es {resultado}')
    
if __name__ == "__main__":
    prueba()
    
    