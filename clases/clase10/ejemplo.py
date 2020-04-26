import funciones_lectura as helper
##Leimos el archivo
lineas= helper.leer_archivo("Libro.txt")
#Lo mostramos linea por linea
helper.mostrar_lineas(lineas)

Texto = ["Hola este es mi primer archivo creado en python\n",
"Espero que funcione bien!! \n",
"Espero que funcione bien!! \n",
"Espero que funcione bien!! \n",
"Espero que funcione bien!! \n",
"Espero que funcione bien!! \n",
"más contenido"]
helper.escritura_archivo("Intento1.txt",Texto)
helper.agregar_lineas_archivo("noticia.txt","\n16 de Abril")