#---------------MENSAJE-----------#
PREGUNTA_NUMERO_DE_PACIENTES = "ingrese numero de paciente \n "
MENSAJE_BIENVENIDO = "Bienvenida"
MENSAJE_RIEGO_BAJO = "estas en riego bajo "
MENSAJE_RIEGO_MEDIO = "estas en riego medio"
MENSAJE_RIEGO_ALTO = "estas en riego alto"
PREGUNTA_PACIENTES_UCI = " ingrese el numero de pacientes en uci \n "
#--------------ENTRADA--------------
_numeroPaciente = 0
_numeroPacienteUCI = 0
#---------------SALIDA---------------
_riesgoOperacional = " "
#--------------VARIABLES-------------
RIESGO_OPERACIONAL = 0
#---------------CODIGO---------------
print (MENSAJE_BIENVENIDO)
_numero_de_paciente = input (PREGUNTA_NUMERO_DE_PACIENTES)
_numeroPacienteUCI = input (PREGUNTA_PACIENTES_UCI)
if ((_numeroPaciente >= 0) and ( _numeroPaciente <=1000) ) :
    print (MENSAJE_RIEGO_BAJO)
elif ( (_numero_de_paciente<= 5000) ) :
    print (MENSAJE_RIEGO_MEDIO)
else: 
    print (MENSAJE_RIEGO_ALTO)

