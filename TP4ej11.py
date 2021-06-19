################
# Mariela Carriqueo - @MCarriqueo
# TP4 Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    """
    Esta función indica si la palabra o frase ingresada es un palíndromo
    """
    texto = str(input(texto+ "  " ))
    for i in range (len(texto)):
        texto = texto.replace(" ", "")
        b= texto[::-i-1]
        if texto == b:
            return True
        else:
            return False
    

def prueba():
    txt = ('Ingrese una palabra o frase')
    tx = es_palindromo(txt)
    print({tx})
    
    
 
    
if __name__ == "__main__":
    prueba()
     
        
    
   
                