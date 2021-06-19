################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from TP4ej1 import ingreso_entero
def es_primo(numero):
    """
    Esta función indica si un número es primo
    """
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True

def prueba():
    num = ingreso_entero('Ingrese un número')
    valor = es_primo(num)
    print(f'{valor}')
    
if __name__ == "__main__":
    prueba()
     
        
    
