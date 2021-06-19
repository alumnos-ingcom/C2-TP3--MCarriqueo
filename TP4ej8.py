################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4ej1 import ingreso_entero

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función ordena de mayor a menor 3 variables
    """
    if uno > dos and uno > tres:
        mayor = uno
        if dos > tres:
            segundo = dos
            tercero = tres
        else:
            segundo = tres
            tercero = dos
    elif dos > uno and dos > tres:
        mayor = dos
        if uno > tres:
            segundo = uno
            tercero = tres
        else:
            segundo = tres
            tercero = uno
    else:
        mayor = tres
        if uno > dos:
            segundo = uno
            tercero = dos
        else:
            segundo = dos
            tercero = uno
    return (mayor, segundo, tercero)
            
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función ordena de menor a mayor 3 variables
    """
    if uno < dos and uno < tres:
        menor = uno
        if dos < tres:
            segundo = dos
            tercero = tres
        else:
            segundo = tres
            tercero = dos
    elif dos < uno and dos < tres:
        menor = dos
        if uno < tres:
            segundo = uno
            tercero = tres
        else:
            segundo = tres
            tercero = uno
    else:
        menor = tres
        if uno < dos:
            segundo = uno
            tercero = dos
        else:
            segundo = dos
            tercero = uno
    return (menor, segundo, tercero)
            
    
def prueba():
    uno = ingreso_entero('Ingrese un valor')
    dos = ingreso_entero ('Ingrese otro valor')
    tres = ingreso_entero ('Ingrese un tercer valor')
    valor =ordenar_mayor_a_menor (uno, dos, tres)
    print(f'el orden de mayor a menor es {valor}')
    
    
def prueba2():
    uno = ingreso_entero('Ingrese un valor')
    dos = ingreso_entero ('Ingrese otro valor')
    tres = ingreso_entero ('Ingrese un tercer valor')
    valor =ordenar_menor_a_mayor (uno, dos, tres)
    print(f'el orden de menor a mayor es {valor}')

if __name__ == "__main__":
    prueba2()
     
    