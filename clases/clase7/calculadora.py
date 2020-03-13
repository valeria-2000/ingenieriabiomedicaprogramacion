#---------------------MENSAJE------------------
PREGUNTA_DADOS1 = "ingrese nunero dado 1 \n "
PREGUNTA_DADOS2 = "ingrese numero dado 2 \n "
MENSAJE_SUMA = "tu suma da como resultado"
MENSAJE_RESTA = "tu resta da como resultado "
MENSAJE_MULTIPLICACION = " tu multiplicacion da como resultado"
MENSAJE_DIVIDIR = "tu division da como resultado"
MENSAJE_DESPEDIDA = "gracias por jugar conmigo"
#---------------------ENTRADA------------------
_numeroDado1 = 0
_numeroDado2 = 0 
#---------------------CODIGO-------------------
_numeroDado1 =  int (input (PREGUNTA_DADOS1))
_numeroDado2 = int (input (PREGUNTA_DADOS2))
def sumar(x,y) :
    suma = x+y
    return suma
resultado = sumar(_numeroDado1, _numeroDado2)
print(MENSAJE_SUMA)
print (resultado)

def restar (x,y) :
    resta = x-y
    return resta
resultado = restar(_numeroDado1, _numeroDado2)    
print(MENSAJE_RESTA)
print (resultado)

def multiplicar (x,y) :
    multiplicar = x*y
    return multiplicar
resultado = multiplicar(_numeroDado1 ,_numeroDado2)    
print(MENSAJE_MULTIPLICACION)
print (resultado)

def dividir (x,y) :
    divide = x/y
    return divide
resultado = dividir(_numeroDado1,_numeroDado2)    
print (MENSAJE_DIVIDIR)
print (resultado)
print (MENSAJE_DESPEDIDA)


