class canguros ():
    def __init__(self,edad,identificacion,saltos,totalcanguros) :
        self.edad = edad
        self.identificacion = identificacion
        self.totalcanguros = totalcanguros
        self.saltos = saltos     
       

class cuidador ():
    def __init__(self,nombre,identificacion) :
        self.nombre = nombre
        self.identificacion = identificacion
    def alimentar(self,totalcanguros) :
        print("alimente {}".format(totalcanguros)) 
        
class jefe(cuidador):
    def __init__(self,cuidador):
        self.nombre = cuidador.nombre
    def contratar(self,nombre) :
        print("contrate {}".format(nombre))
    def mensaje(self,mensaje_1):
        print("el jefe dijo {}".format(mensaje_1))
    

cuidador1 = cuidador("Valeria",1010150364)
cuidador2 = cuidador("Sofia",1234567890)
cuidador3 = cuidador("Daniel",4567891209)
cuidador4 = cuidador("Sebastian",1987654321)
cuidador5 = cuidador("Sara",6787653421)

canguro1 = canguros(5,2341127890,10,4)
canguro2 = canguros(4,5678765123,12,3)
canguro3 = canguros(2,3890123256,14,5)
canguro4 = canguros(9,1111111111,34,4)
canguro5 = canguros(6,8689088888,23,2)
canguro6 = canguros(7,5555445565,67,22)
canguro7 = canguros(3,3234344444,21,44)
canguro8 = canguros(1,1112223333,18,55)
canguro9 = canguros(8,7874555326,19,66)
canguro10 = canguros(1,9999997875,30,33)
print (canguro1.saltos)


jefe1 = jefe(cuidador1)

cuidador1.alimentar(4)
jefe1.mensaje("ahora estan en semana santa")
jefe1.contratar("luis")

