#1.grafica
#------------MESAJES-----------------#
PREGUNTA_NOMBRE = "Ingrese el archivo que quieres graficar \n "

#------------CODIGO------------------#
import matplotlib.pyplot as plt
import pandas as p 
def validador_archivo(PREGUNTA_NOMBRE):
    assert (open (archivoUsuario) )
    return False
validador = True
while (validador):
    archivoUsuario = input (PREGUNTA_NOMBRE)
    try:
        validador = validador_archivo(PREGUNTA_NOMBRE)
        grafica_1 = p.read_csv(archivoUsuario,encoding='UTF-8',header=0, delimiter=";").to_dict()
        x = list (grafica_1["muestra"].values())
        y = list (grafica_1 ["valor"].values())
        plt.plot(x,y)
    except FileNotFoundError :
        print("ingresaste un archivo que no existe")

PREGUNTA_TITULO = "Ingrese el titulo que le desea colocar a la grafica \n"
PREGUNTA_EJE_X = "Ingrese el titulo que le desea colocar al eje x \n"
PREGUNTA_EJE_y = "Ingrese el titulo que le desea colocar al eje y \n"

titulo = input (PREGUNTA_TITULO)
titulo_x = input (PREGUNTA_EJE_X)
titulo_y = input (PREGUNTA_EJE_y)
plt.title(titulo)
plt.xlabel(titulo_x)
plt.ylabel(titulo_y)
plt.savefig(archivoUsuario + ".png")
plt.show()

#------------------------------------------------------------------------------------------#
#2.#------------MESAJES-----------------#
PREGUNTA_NOMBRE = "Ingrese su nombre \n "
PREGUNTA_EDAD = "Ingreses su edad \n"
PREGUNTA_PESO = "Ingrese su peso \n"
PREGUNTA_ESTATURA = "Ingrese su estatura \n"

#-------------VARIABLE------------------#
IMC = 0.0
#--------------ENTRADA------------------#
_nombreUsuario = " "
_edadUsuario = 0
_pesoUsuario = 0.0
_estaturaUsuario = 0.0
#--------------CODIGO-------------------#

_nombreUsuario = input (PREGUNTA_NOMBRE)

try:
    _edadUsuario = int (input (PREGUNTA_EDAD))
except ValueError:
    print("ingresaste mal el peso")
try:
    _pesoUsuario = float (input (PREGUNTA_PESO))
except ValueError:
    print("ingresaste mal el peso")
try:
    _estaturaUsuario = float (input (PREGUNTA_ESTATURA))
except ValueError:
    print("ingresaste mal la estatura ")

IMC = (_pesoUsuario/_estaturaUsuario**2)
print ("Su imc es de {}".format (IMC) )

#-----------------------------------------------------------------------------------------#
#3.
#------------CODIGO-----------------#
import matplotlib.pyplot as plt

archivos = {
    "grafica" : ["ecs" , "ppg", "eeg"] ,
    "picos" : [9,9,10]
}
plt.bar (archivos["grafica"], archivos["picos"], color = "r")
plt.title("CANTIDAD DE PICOS DE LAS SEÑALES ")
plt.xlabel ("Archivos ")
plt.ylabel ("Numero de picos")
plt.savefig("comparacion_de_picos.png")
plt.show()
#-----------------------------------------------------------------------------------------#
#4.Grafico de pie 
labels = 'Habitacion', 'Sala' , 'Cocina' , 'Balcon '
sizes = [45,30,10,15]
explode = (0.1,0,0,0)
plt.pie(sizes, explode = explode , labels = labels, shadow = True, startangle = 45)
plt.title ("Cuarentena")
plt.savefig("covid_y_Su_cuarentena.png")
plt.show()
#-----------------------------------------------------------------------------------------#
#5. 

Supervisado_y_no_supervisado =  """Siento que cuando uno esta supervisado como que nuestro cerebro esta mas concentrado mientras que si estamos en la casa y no nos supervisan,
nuestro cerebro se puede desconcentra super facil, tal vez supervisado no hay tanta flexibilidad a lo hora de entregar trabajos como si lo es no supervisado,y supervisado las clases son mas personalizadas que virtualmente por decirlo asi, pero todo va en cada persona 
en las ganas que quiera aprender, en las ganas de disfrutarse su carrera, en la actitud que le pongas a las clases,a los parciales a los trabajos,todo esta en cada estudiante."""
print(Supervisado_y_no_supervisado)