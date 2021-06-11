################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 4
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero

def compara (numero, otro_numero):
    """
    Esta funcion compara dos valores e indica si el primero es mayor, menor o igual al segundo valor
    """
    if numero > otro_numero:
        return 1
    elif numero < otro_numero:
        return -1
    else:
        return 0

def prueba():
    num = ingreso_entero('Primer número')
    num2 = ingreso_entero('Segundo número')
    valor = compara(num,num2)
    print(f' el resultado de la comparacion es {valor}')
    
  
    
if __name__ == "__main__":
    prueba()
     
    
    
        
    
    