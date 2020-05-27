#---------------------------------------------------------------------------------------------------#
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
#3. #------------MESAJES-----------------#
PREGUNTA_ARROZ = "cuantos kilos tiene de arroz \n "
PREGUNTA_LENTEJA = " cuantos kilos tiene de lentejas\n"
PREGUNTA_FRIJOL = "cuantos kilos tiene de frijoles \n"
PREGUNTA_PAPA = "Cuantos kilos tiene de papa \n"

#--------------ENTRADA-------------------#
_kilosArroz= 0
_kilosLentejas = 0
_kilosFrijol = 0
_kilosPapa = 0

#--------------CODIGO---------------------#
import matplotlib.pyplot as plt
try:
    _kilosArroz= int (input (PREGUNTA_ARROZ))
    _kilosLentejas = int (input (PREGUNTA_LENTEJA))
    _kilosFrijol = int (input (PREGUNTA_FRIJOL))
    _kilosPapa = int (input (PREGUNTA_PAPA))
    pregunta = {
    "nombres" : ["Arroz", "Lenteja" , "Frijol" ,"Papa"] ,
    "kilos" : [_kilosArroz, _kilosLentejas, _kilosFrijol , _kilosPapa]
    }
    plt.bar (pregunta ["nombres"],pregunta ["kilos"],color = "r", alpha = 0.2)
except ValueError:
    print("Entreda no valida")
    
plt.savefig("Mercado.png")
plt.show()

#------------------------------------------------------------------------------------------#
#4.texto finalizado en punto 

def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while (validador):
    parrafo =  input('cuentame como te has sentido .')
    try:
        validador = validador_parrafo(parrafo)
    except AssertionError:
        print("Entrada no válida, intruduzca el texto pero acuerdate en finalizar en punto")


#-----------------------------------------------------------------------------------------#
# 5.Grafico de  pie 

labels = 'Leche', 'Huevo', 'Vino' , 'Arroz','Queso', "Salchichas"
sizes = [12,8,4,26,30,20]
explode = [0,0,0,0,0.1,0]
plt.pie (sizes, explode=explode, labels=labels , shadow=True, startangle=45 ,)
plt.title ("Compras en la tienda")
plt.savefig ("compras_en_la_tienda.png")
plt.close
plt.show()