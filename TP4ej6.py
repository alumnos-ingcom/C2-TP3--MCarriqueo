################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero
def minimo(lista):
    """
    Esta función devuelve el menor valor de un lista
    """
    menor = lista[0]
    for numero in lista:       
        if menor > numero:
            menor = numero
        
        
def maximo(lista):
    """
    Esta función devuelve el mayor valor de un lista
    """
    mayor = lista[0]
    for numero in lista:       
        if mayor < numero:
            mayor = numero
            

def prueba():
    num=ingreso_entero('Ingrese un número')
    num2=ingreso_entero('Ingrese número siguiente')
    num3=ingreso_entero('Ingrese número siguiente')
    num4=ingreso_entero('Ingrese número siguiente')
    lista =[num,num2,num3,num4]
    print(lista)
    valor = maximo(lista)
    print(f'el número menor es {valor}')
    
if __name__ == "__main__":
    prueba()
        
       
    
