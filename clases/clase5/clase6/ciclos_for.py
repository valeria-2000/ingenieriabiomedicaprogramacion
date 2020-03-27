#-------------variable-----------
# _cantidadsaltos = int (input("ingrese la cantidad de saltos :"))
# for i in range (4) :
#     print(i)
# for i in range(_cantidadsaltos) :
#     print ("el canguro da su salto numero",i+1)
    
# DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes"]    
# for dia in DIAS :
#     print(dia)


NOMBRES = ["OCTAVIO", "LUCAS" , "ABEL", "ISABELA" ," KATHER", "MARIA"]
EDADES = [14,18,22,26,34,38]
print(len(NOMBRES), len(EDADES))
for i in range (len(NOMBRES)) :
    if EDADES [i] >= 18 :
        print (i, "LA PERSONA" ,NOMBRES[i], "ES MAYOR")

        
sumaEdades = 0
for edad in EDADES :
    sumaEdades += edad
print (sumaEdades)          
