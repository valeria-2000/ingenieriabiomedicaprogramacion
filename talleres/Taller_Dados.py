import random 
#---------------mensaje------------
MENSAJE_ACIERTO = " MUY BIEN!!!!! al lanzar tus dos dados, te da 12"  
MENSAJE_FALLO = "sigue intentando"
NUMERO_DADO1 = 0
NUMERO_DADO2 = 0
NUMERO_DESEADO = 12
suma = 0
#---------------codigo------------
while (suma != NUMERO_DESEADO): 
    print (MENSAJE_FALLO)
    NUMERO_DADO1= random.randint (1,6)
    NUMERO_DADO2 = random.randint (1,6)
    suma = NUMERO_DADO1 + NUMERO_DADO2
    print (suma)
print (MENSAJE_ACIERTO)




