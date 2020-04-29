diccionario = {}
medios_transporte = {}
medios_transporte ["carros"] = ["BMW", "Audi"," Mazda", "Toyota"]
medios_transporte ["motos"] = ["AKT" , " Honda ", "CDI"]
print(medios_transporte)
print (" los elementtos que componen la llave carros son : {}".format (medios_transporte ["carros"]))

#para obtener todas las llaves de un diccionario 
print(list(medios_transporte.keys()))

# para obtener todo lo que halla dentro de esas llaves
print (list(medios_transporte.values()))
valores = list (medios_transporte.values())
print (valores [0])

#generar una copia sin afectar el original 
diccionario_copia = diccionario.copy()
print(diccionario_copia)

#eliinar la ultima llave agregada 
#diccionario_copia.popitem()
#print (diccionario_copia)

#agregar una llave o si existe, sobre es escribir su valor 
diccionario_copia.setdefault("computadoras" , ["apple", "dell"])
print (diccionario_copia)
print (diccionario_copia.setdefault ("computadoras", ["apple", "dell" ,"IBM"]))
print (diccionario_copia)

#limpiar el contenido de un diccionario 
diccionario_copia.clear()
print(diccionario_copia)

#eliminar un componente de la lista
diccionario_copia.pop("carros")

#obtener directamente una lista 

print (medios_transporte.get("carros"))
