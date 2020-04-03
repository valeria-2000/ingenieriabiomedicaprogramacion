#------------mensaje---------------
PREGUNTA_IDENTIFICACION = "el numero de identificacion de este canguro es : "
MENSAJE_EDAD = "este canguro tiene"
PREGUNTA_CUIDADOR = " el nombre del cuidado es : "
PREGUNTA_IDENTIFICACION = " EL NUMERO DE INDETIFICACION DEL CUIDADO ES : "


class canguros ():
    def __init__(self,edad,identificacion,saltos,totalcanguros) :
        self.edad = edad
        self.identificacion = identificacion
    def atributos(Self):
        print(PREGUNTA_IDENTIFICACION,self.edad)
        print(MENSAJE_EDAD, self.edad, "años")
    def saltar(self,cantidas_Saltos):
        for i in range (cantidad_saltos):
            print( " el canguro ha dado" , i+1, "saltos")
        
canguro1 = canguros(5,2341127890)
canguro2 = canguros(4,5678765123)
canguro3 = canguros(2,3890123256)
canguro4 = canguros(9,1111111111)
canguro5 = canguros(6,8689088888)
canguro6 = canguros(7,5555445565)
canguro7 = canguros(3,3234344444)
canguro8 = canguros(1,1112223333)
canguro9 = canguros(8,7874555326)
canguro10 = canguros(1,9999997875)


class cuidador ():
    def __init__(self,nombre,identificacion) :
        self.nombre = nombre
        self.identificacion = identificacion
    def mostrar_atributos(self):
        print(PREGUNTA_CUIDADOR,self.nombre)
        print(PREGUNTA_IDENTIFICACION,self.identificacion)
class alimentar() :
    def __init__(Self,nombre):
        self.nombre = nombre
    def alimentar_canguros(self,cantidad_canguros_alimentados):
        for i in range (cantidad_canguros_alimentados):
            print("el cuidador ha alimentado", i+1,"canguros")

            


cuidador1 = cuidador("Valeria",1010150364)
cuidador2 = cuidador("Sofia",1234567890)
cuidador3 = cuidador("Daniel",4567891209)
cuidador4 = cuidador("Sebastian",1987654321)
cuidador5 = cuidador("Sara",6787653421)

cuidador1.mostrar_atributos()
cuida