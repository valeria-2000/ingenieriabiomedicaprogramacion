class Humano ():
    def __init__(self,nombre,estatura,peso,genero,edad):
        print("Hola")
        self.raza = "Ser humano"
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.genero = genero 
        self.edad = edad 
        print ("Hola a todos soy un", self.raza, "mi nombre es", self.nombre)
    def mostrar_atributos(self):
       print ("mi nombre es", self.nombre)
       print ("mi edad es",self.edad)
       print ("mi estatura es",self.estatura)
       print ("mi genero es", self.genero)
       print ("mi peso es", self.peso)
        
ser_humano_1 = Humano("valeria",1.60,53,"femenino",19) 
ser_humano_2 = Humano("daniel",1.80,66,"masculino",19)
ser_humano_3 = Humano("sarita",1.63,55,"femenino",19)

ser_humano_1.mostrar_atributos()
ser_humano_2.mostrar_atributos()
ser_humano_3.mostrar_atributos()