#--------------------------MENSAJE------------------------------#
PREGUNTA_PROCEDENCIA = "ingrese su procedencia : "
PREGUNTA_TEMPERATURA_PACIENTE = "ingrese su temperatura : "
MENSAJE_SALUDABLE = "estas saludable"
MENSAJE_ESTADO_DE_HIPOTERMIA = "estas en estado de hipotermia"
MENSAJE_ESTADO_ALERTA = "estas en estado de alerta"
MENSAJE_ESTADO_PELIGRO = "estas en estado de peligro"
MENSAJE_OBSERVACION= "estas en estado de obervacion "
#--------------------------ENTRADA---------------------------------
_procedenciaUsuario = " "
_temperaturaUsuario = 0.0
#--------------------------SALIDA----------------------------------
_estadoPaciente = " "
#--------------------------CODIGO----------------------------------
_procedenciaUsuario = input (PREGUNTA_PROCEDENCIA)
if ((_procedenciaUsuario == "china" ) or (_procedenciaUsuario == "iran") or (_procedenciaUsuario == "italia" )) :
    print (MENSAJE_OBSERVACION)
else:
    _temperaturaUsuario = float (input(PREGUNTA_TEMPERATURA_PACIENTE) )
    if ((_temperaturaUsuario <36 )) :
        print (MENSAJE_ESTADO_DE_HIPOTERMIA)
    elif ((_temperaturaUsuario >=36 ) and (_temperaturaUsuario <=38.4)) :
        print (MENSAJE_SALUDABLE)
    elif ((_temperaturaUsuario >=38.5) and (_temperaturaUsuario <=40)) :
        print (MENSAJE_ESTADO_ALERTA)   
    else:
        print (MENSAJE_ESTADO_PELIGRO)
