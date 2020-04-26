nombre = ["valeria","sara","daniel","geraldin","carlos" ]
edad = [19,18,20,22,25]
genero = ["femenino","femenino","masculino","femenino","masculino"]
colegio = ["jose","salazar","gabo", "jose","gabo"]

nombre = ["luis","carlos"]
edad = [27,30]
nivel academico = ["maestria","doctorado"]
pregunta_numero = """
        1- mostrar los atributos de los estudiantes
        2- mostrar los atributos de los profesores
        3- mostrar los atributos del director
        4- salir 
"""
def mostrar_cuatro_lista(lista1,lista2,lista3,lista4):
   posicion = 1
   for elemnto in range(len(lista1)):
       print(lista1[elementto],lista2[elemento,lista3[elemento,lista4[elemento])
       posicion +=1
    return()
def mostrar_tres_listas (lista1,lista2,lista3):
    posicion = 1
    for elemento in range(len(lista1)):
        print(lista1[elemento],lista2[elemento,lista3[elemento])
    return()
_eleccion_usuario = 0 
while(_eleccion_usuario !=4):
    _eleccion_usuario = int(input(pregunta_numero))
    if (_eleccion_usuario ==1):

        

class estudiantes():
    def __init__(self,nombre,edad,genero,colegio):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero 
        self.colegio = colegio 
    def asistir_clase(self, cantidad_clases):
        for i in range(cantidad_clases):
            print("asisti", i+1,"clases")

class profesores():
    def __init__(self,nombre,edad,nivel_educativo):
        self.nombre = nombre
        self.edad = edad
        self.nivel_educativo = nivel_educativo
    def dictar_clase(self,cuantas_clases_dara):
        for i in range(cuantas_clases_dara):
            print("dictare", i+1,"clases")
            
        

class directores (profesores):
    def contratar_profesores(self,cuantos_contrato):
        for i in range(cuantos_contrato):
            print("contrate" , i+1  , "profesores")
            





    

estudiante_1 = estudiantes("valeria",19,"femenino","jose antonio galan")
estudiante_2 = estudiantes("sara",18,"femenino","salazar herrera")
estudiante_3 = estudiantes("daniel",20,"masculino","gabo")
estudiante_4 = estudiantes("santiago",22,"masculino","jose antonio galan")        
estudiante_5 = estudiantes("geral",25,"femenino","gabo")
estudiante_1.asistir_clase(8)

profesor_1 = profesores ("luis",27,"maestria")
profesor_2 = profesores ("carlos",30,"doctorado")
profesor_1.dictar_clase(5)

director_1 = directores("samuel", 34 ,"doctorado")
director_1.contratar_profesores(2)


listaNombrestudiantes = []
lsitaEdesestudiantes = []
listaGeneroestudiante = []
listaEstudioestudiante = []


listaNombreprofesores = []
listaEdaesprofesores = []
listaNivelprofesores = []

