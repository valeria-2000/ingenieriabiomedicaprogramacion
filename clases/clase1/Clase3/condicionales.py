#------------Mensajes-----------#
PREGUNTA_NOMBRE = "ingrese su nombre \n "
PREGUNTA_EDAD = "ingrese porfavorshito su edad  \n "
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_TOCAYO = "Hola hermana somos tocayas"
MENSAJE_JOVEN = "Eres Joven"
MENSAJE_ADULTO = "Eres Adulto"
MENSAJE_VIEJO = "Eres Viejo"
MENSANJE_DESPEDIDA = "CHAO"

#------------VARIABLES-----------
NOMBRE_PERSONAL = "Valeria"
#-------------ENTRADAS------------
_nombreUsuario = " "
_edadUsuario = 0
#-------------CODIGO------------
print(PREGUNTA_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) :
    print(MENSAJE_TOCAYO)
print (MENSANJE_DESPEDIDA)    
_edadUsuario = int (input(PREGUNTA_EDAD))

if ((_edadUsuario >= 0) and (_edadUsuario <= 25)) :
    print(MENSAJE_JOVEN)
elif ((_edadUsuario >= 26) and (_edadUsuario <= 65)) :
    print (MENSAJE_ADULTO)
else:     
    print (MENSAJE_VIEJO)
print (MENSANJE_DESPEDIDA) 


        