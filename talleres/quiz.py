#-------------------MENSAJE-----------------
MENSAJE_BIENVENIDO = "Bienvenida"
PREGUNTA_NUMERO = """
        ingrese un numero 
        entero 
        entre 1-4 
        : """
PREGUNTA_CELSIUS = "ingrese la cantidad de grados calcius a convertir :"
MENSAJE_CELSIUS = "la conversion no es necesaria"
MENSAJE_ERROR = "La entrada fue erronea "
#--------------------ENTRADA------------------
_nuemeroIngresado = 0 

#--------------------CODIGO-------------------
print (MENSAJE_BIENVENIDO)
_nuemeroIngresado = int (input (PREGUNTA_NUMERO))
while (_nuemeroIngresado == 1) :
        respuesta = input ("deseas conertirlo f -> fahrenheit k -> kelvin :" )
        if (respuesta == "f") :
                C = float(input (PREGUNTA_CELSIUS))
                F = 9 / 5 * C + 32
                print(C,"grados celsius equivale a ", F, "grados fahrenheit.")
        elif (respuesta == "c"):
                C = float(input (PREGUNTA_CELSIUS))
                print(MENSAJE_CELSIUS)
        else:        
                C = float(input (PREGUNTA_CELSIUS))
                K = C + 273.15
                print(C,"grados celsius equivale a ", K, "grados kelvin.")
        _nuemeroIngresado = int (input (PREGUNTA_NUMERO))


        
 
       
              

