# Contar caracteres: Escribe una función recursiva que cuente cuántas veces aparece un carácter específico en una cadena.
#Por ejemplo, cuántas veces aparece la letra 'a' en "anaranjada".


def recursive(numero_caracteres):
   
    if len(numero_caracteres) == 0:
        return 0
    
    else:
   
        letra = 'a'
        posicion =  numero_caracteres[-1].find(letra)
        
        if posicion == -1:
            return 1 + recursive(numero_caracteres[:-1])
         
        else:
            return  recursive(numero_caracteres[:-1])



def contar_caracteres(numero_caracteres):
    resultado = recursive(numero_caracteres)

    print(resultado)


contar_caracteres("anaranjada")
