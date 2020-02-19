#-------------Mensajes----------------#
PREGUNTA_NOMBRE="ingrese su nombre : "
MENSAJE_BIENVENIDO="Bienvenido"
PREGUNTA_EDAD="ingrese su edad : "
MENSAJE_EDAD="ingrese su edad "
PREGUNTA_ESTATURA="ingrese su estatura"
#-------------------------------------
_nombrePersona = input( PREGUNTA_NOMBRE )
print(MENSAJE_BIENVENIDO,_nombrePersona, MENSAJE_BIENVENIDO)
_edadPersona =int(input(PREGUNTA_EDAD  ))
print(MENSAJE_EDAD,_edadPersona)
print (type(_edadPersona))
_estaturaPersona =float(input(PREGUNTA_ESTATURA ))
print(PREGUNTA_ESTATURA,_estaturaPersona)
print (type(_estaturaPersona))
