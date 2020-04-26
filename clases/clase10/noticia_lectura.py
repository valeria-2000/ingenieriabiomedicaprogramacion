import funciones_lectura as support
lineas= support.leer_archivo("noticia.txt")
support.mostrar_lineas(lineas)

Texto = ["Si nos fijamos en el ámbito profesional  \n "
"vemos que se habla y se lee en inglés en los ámbitos mas importantes de la vida laboral: economía, industrial, negocios, comercio internacional, entre otros\n",
"y si tenemos un segundo idioma independientemente si es o no ingles en cual apoyarnos \n"
"se nos van abrir puertas que ni nosotros mismo creiamos que seria posible.\n"
"y pienso que si vemos a nivel laboral \n "
"el manejo de varias lenguas es transcendental para tener una carrera profesional más fructífera.   \n",
"y si quieres trabajar en el extranjero \n"
"debes ser consciente de la importancia que tiene el inglés y hacer todo lo posible para lograr alcanzar un buen nivel de comprensión y expresión tanto oral como escrita.\n",
"Sería ideal que todas las personas,sin importar el perfil o el cargo, aprendieran varias lenguas, \n"
"debido a que en un mundo globalizado como el de hoy, donde los trabajos son cada vez más internacionales, sin importar el sector, la lengua materna no es suficiente."]

support.escritura_archivo("opinion.txt",Texto)
support.agregar_lineas_archivo("noticia.txt","\n4 de noviembre,\nel tiempo")
