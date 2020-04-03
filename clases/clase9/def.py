#definiendo una funcion llamada  linedesign 
def linedesign():
    print("#"*60)
    return "satisfactorio"

#entrada : son unas variables que se utilizan en las funciones para realizar procesos
#salida : es lo que devolvemos al ejecutar una funcion 

def suma(a,b):
    resultado = a+b
    return resultado

#entrada la codigo 

devuelve = linedesign()
print(devuelve)


resultado = suma(2,4)
print(resultado)



#listas
class TortaRedonda():
    def __init__(self,sabor,altura,temperatura,area) :
        self.forma = "redondas"
        self.sabor = sabor
        self.altura = altura
        self.temperatura = temperatura
        self.area = area

class Cocinero():
    def __init__(self,nombre):
        self.nombre = nombre
    def dividir_torta(self,personas,area):
        print("voy a dividir la torta")
        size = area/personas
        return size

 #Herencia        
class Repostero(Cocinero):
    def crear_torta(self,sabor,altura,temperatura,area) :
        print("procedo a crear torta")   
        torta = TortaRedonda(sabor,altura,temperatura,area)
        return torta

torta1 = TortaRedonda("chocolate", 10,42.8,100)        
torta2 = TortaRedonda("vainilla", 20,52.7,450)  

print ("el sabor de la primera torta es ", torta1.sabor)
print ("el sabor de la segunda torta es ", torta2.sabor)
print ("la forma de la primera torta es ", torta1.forma)
print ("la forma de la segunda torta es ", torta2.forma)
#hacer la accion
cocinero1 = Cocinero("Daniel")
personas = 12
porcion = cocinero1.dividir_torta(personas,torta1.area)
print ("Hola a todos soy", cocinero1.nombre, " y dividi la torta para ", personas ,"personas")
print ("el tamaño de la porcion para cada uno es ", porcion)

cocinero2 = Repostero("Mafer")
torta_creada = cocinero2.crear_torta("chocoalmendra",20,60,200)
print(torta_creada.sabor,torta_creada.forma)

personas_segundo_grupo = 10
porcion2 = cocinero2.dividir_torta(personas_segundo_grupo,torta_creada.area)
print ("Hola a todos soy", cocinero2.nombre, " y dividi la torta para ", personas_segundo_grupo,"personas")
print ("el tamaño de la pocion para cada uno es",porcion2)