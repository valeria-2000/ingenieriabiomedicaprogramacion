#------------MESAJES-----------------#
PREGUNTA_NOMBRE = "ingrese su nombre \n "
MENSAJE_BIENVENIDO = "Bienvenido"
PREGUNTA_PESO = "ingrese su peso"
PREGUNTA_ESTATURA = "ingrese su estatura"
MESANJE_DESPEDIDA = "despedida "
MENSAJE_BAJO_PESO = "eres flaquito"
MENSAJE_SALUDABLE = "estas super saludable"
MENSAJE_SOBREPESO = "eres gordito"
MENSAJE_OBESIDAD_MORBIDA = "vas a morir"
MENSAJE_TOCAYO = "somos tocayas obesas"
#-------------VARIABLE---------------
NOMBRE_PERSONAL = "valeria"
IMC = 0.0
#--------------ENTRADA----------------
_nombreUsuario = " "
_pesoUsuario = 0.0
_estaturaUsuario = 0.0
#--------------CODIGO-----------------
print (MENSAJE_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
_pesoUsuario = float (input (PREGUNTA_PESO))
_estaturaUsuario = float (input (PREGUNTA_ESTATURA))
IMC = (_pesoUsuario/_estaturaUsuario**2)
print (IMC)
if ((IMC >=12) and (IMC <=18)) :
    print (MENSAJE_BAJO_PESO)
elif ((IMC >=19) and (IMC <=24)) :
    print (MENSAJE_SALUDABLE)        
elif ((IMC >=30) and (IMC <=39)) :
    print (MENSAJE_SOBREPESO) 
else:
    print (MENSAJE_OBESIDAD_MORBIDA)
    print (MENSAJE_TOCAYO) 
print (MESANJE_DESPEDIDA)    