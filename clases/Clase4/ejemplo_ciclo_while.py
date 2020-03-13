# numero = 0
# NUMERO_DESEADO = 12
# while (numero < NUMERO_DESEADO) : 
 #   numero = numero +1
 #   print(numero)
# print (numero)  
import random   
PREGUNTA_NUMERO = """
      Ingrese un numero 
      entero
      entre el 1-10
      : """
MENSAJE_FALLO = " FALLASTE!!! INTENTELO DE NUEVO"  
MENSAJE_ACIERTO = "FELICIDADES SABES MI NUMERO FAVORITO"  
MENSAJE_MAYOR = "ESTAS CERCA EL NUMERO QUE INGRESO ES MAS GRANDE "  
MENSAJE_MENOR = "ESTAS CERCA EL NUMERO QUE INGRESO ES MENOR "
NUMERO_FAVORITO = random.randint (1,10)
_numeroIngresado = int (input (PREGUNTA_NUMERO))
while (_numeroIngresado != NUMERO_FAVORITO) :
    print(MENSAJE_FALLO)
    if (_numeroIngresado >NUMERO_FAVORITO) :  print (MENSAJE_MAYOR)
    else : print (MENSAJE_MENOR)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)    