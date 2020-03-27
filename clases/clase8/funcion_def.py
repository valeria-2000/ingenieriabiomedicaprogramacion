def hablar (mensaje):
    print (mensaje)
    return "exitoso"
def Validar_clave (CLAVE_REAL, _claveIngresada) :
    if (CLAVE_REAL == _claveIngresada) :
        print ("ingreso exitoso" )
        STATE = "clave valida" 
    else :
        print ("clave incorrecta")     
        STATE = "clave invalida"
    return STATE

def mostrar_lista(lista):
    contador =1
    for elemento in lista:
        print(contador, "-",elemento)
        contador += 1
def mostrar_dos_listas(lista_1,lista_2) :   
    if (len(lista_1) == len(lista_2))  :
        print("elemento","precio")
        for i in range(len(lista_1))  :
            print(lista_1[i],"$",lista_2[i])

    else:
        print("no se puede mostra uno a uno")  


def bienvenida(): print ("Bienvenido al codigo")  

def ingresar():
    intentos =0
    estado = Validar_clave(1234, int(input("ingrese la clave : ")))
    intentos += 1
    while (estado != "clave valida" and intentos<3) :
        estado = Validar_clave(1234, int(input("ingrese la clave : ")))
        intentos += 1
    return estado     

bienvenida()

if ingresar() == "clave valida" :
    comidas = ["carne","pollo","huevos","queso"]
    precios = [5000,6000,2000,1700]
    mostrar_lista(comidas)
    mostrar_dos_listas(comidas,precios)
else:
    print("lo sentimos usted no ingreso correctamente la contraseña,saliendo del programa")





intentos =0
estado = Validar_clave(1234, int(input("ingrese la clave : ")))
intentos += 1
while (estado != "clave valida" and intentos<3) :
    estado = Validar_clave(1234, int(input("ingrese la clave : ")))
    intentos += 1

    