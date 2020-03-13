#----------lista de nombres-----------------
listaNombres = ["santiago" , 
    "juanes" , 
    "marco" , 
    "elena " , 
    "mch betancur " , 
    "mch mesa" ,
    "leslly" ,
    "ysabella" ,
    "santiago el humilde", 
    "daniel", 
    "mafe" , 
    "david" ,
    "susana" , 
    "daniel h "]
#------------lista de edades-----------------
listaEdades = [20, 17 , 19 , 19 , 19, 18 , 19, 19 , 17 , 20 , 18 , 23 , 20, 29]
#------------------notas---------------------
listaNotas = [ 5.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 4.0 , 5.0]

listaNombres[4] = "maria camila betancur"
listaNombres[5] = "maria camila mesa"
listaNombres.pop(-1)
listaNombres.append("daniel herrera")

_decision = int (input( """
         ingrese :
         1- para ver lista de Nombres
         2- para ver edades
         3-  para ver notas 
         4-   salir 
"""))   
while (_decision !=4) : 
    if (_decision == 1 ):
        print(listaNombres)
    elif (_decision == 2 ):
        print(listaEdades)    
    elif (_decision == 3):
        print (listaNotas)
    else :
        print ("ingrese un valor valido")
    _decision = int (input("""
           ingrese :
           1- para ver lista de Nombres
           2- para ver edades
           3- para ver notas 
           4- salir 
           """))
print("gracias por usar el programa")


           




