
#-------------------MENSAJE-----------------
MENSAJE_BIENVENIDO = "Bienvenida"
PREGUNTA_NUMERO = """
        ingrese un numero
        entero
        entre 1-4
        : """
PREGUNTA_NUMERO_2 = """
        ingrese un numero
        entero
        entre 1-4
        : """       
#--------------------ENTRADA------------------
_nuemeroIngresado = 0 
pesoPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]

#--------------------CODIGO-------------------
print (MENSAJE_BIENVENIDO)
_nuemeroIngresado = int (input (PREGUNTA_NUMERO))
while (_nuemeroIngresado == 1) :
        pesoPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]
        for i in range (len(pesoPacientesIniciales)) :
            presion = (pesoPacientesIniciales[i]* 6 )
            print(pesoPacientesIniciales[i],"tiene una presion de  ",presion, "calculada.")
        _nuemeroIngresado = int (input (PREGUNTA_NUMERO))

while (_nuemeroIngresado == 2) :
        pregunta = input (" Desea añadir nuevos pesos de pacientes? s -> si  n->no : ")
        while (pregunta == "s") :
            pesoPacientesIniciales.append(int(input("ingrese pesos pacientes :")))
            pregunta = input (" Desea añadir nuevos pesos de pacientes? s -> si  n->no : ")
            print (pesoPacientesIniciales)
        _nuemeroIngresado = int (input (PREGUNTA_NUMERO))


while (_nuemeroIngresado == 3) :
        decision = int (input (PREGUNTA_NUMERO_2))
        if (decision == 1) :
            print("la presion mas alta de la lista es {} "
            .format(max (pesoPacientesIniciales)))
        if (decision == 2) :
            print("la presion mas baja es {}"
            .format(min(pesoPacientesIniciales)))
        if (decision == 3) :
            pesoPacientesIniciales.sort(reverse=True)
            print("pacientes ordenado {}".format(pesoPacientesIniciales))
        if (decision == 4) :
            total = len(pesoPacientesIniciales)
            print(total)
            break 


while (_nuemeroIngresado == 4) :
    exit() 