class Persona ():
    def __init__(self,nombre,estatura,genero,peso,edad):
        self.raza = "Ser humano"
        self.name = nombre
        self.stature = estatura
        self.gender = genero 
        self.weight = peso
        self.age = edad 
        print ("Hola a todos soy un", self.raza, "mi nombre es", self.name)

    def mostrar_atributos(self):
       print ("mi nombre es", self.name)
       print ("mi edad es",self.age)
       print ("mi estatura es",self.stature)
       print ("mi genero es", self.gender)
       print ("mi peso es", self.weight)
    def caminar(self,cantidad_pasos):
       for i in range (cantidad_pasos):
           print ("he caminado",i+1,"pasos")

ser_humano_1 = Persona("valeria",1.60,"femenino",53,19)
ser_humano_2 = Persona("sarita",1.62,"femenino",55,19)
    
ser_humano_1.mostrar_atributos()
ser_humano_2.mostrar_atributos()

ser_humano_1.caminar(100)
