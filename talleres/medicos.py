def mostrar_lista(lista):
    contador =1
    for elemento in lista: 
        print(contador, "-",elemento)
        contador +=1
    print("")
        
   
doctores = ["Michelle","Daniel","Valentina","Miguel"]
enfermeras = ["Luciana","Juliana","Sara","Angie"]
lista_de_enfermos = ["Santiago","Sofia","Kevin","Alejandro"]
print ("doctores : " )
mostrar_lista(doctores)
print ("enfermeras : ")
mostrar_lista(enfermeras)
print ("lista de enfermos : ")
mostrar_lista(lista_de_enfermos)

def llenarLista(doctores,enfermeras) :
    decision = input ("desea ingresas mas doctores y enfermeras ? s -> si n -> no : ")
    while (decision == "s"):
        respuesta = input ("a que lista deseas agregar mas? d -> doctores n -> enefermeras :  ")
        if (respuesta == "d"):
            doctores.append(input("ingrese el doctor que quiere agregar : "))
            mostrar_lista(doctores)
            decision = input ("desea ingresas mas doctores y enfermeras ? s -> si n -> no : ")
        else: 
            enfermeras.append(input("ingrese la enfermera que quiere agregar : "))
            mostrar_lista(enfermeras)
            decision = input ("desea ingresas mas doctores y enfermeras ? s -> si n -> no : ")
llenarLista(doctores,enfermeras)    

def mostrar_dos_listas(lista_1,lista_2):
    if(len(lista_1) == len(lista_2)):
        for i in range(len(lista_1)):
            print(lista_1[i],lista_2[i])
    else:
        print("no se puede mostrar uno a uno")        

lista_de_enfermos = ["Santiago","Sofia","Kevin","Alejandro"]
estado_del_enfermo = ["estado grave","estado critico","en recuperacion","estado grave "]
mostrar_dos_listas(lista_de_enfermos,estado_del_enfermo)

