import pandas as p
diccionario = p.read_csv("balance.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print (diccionario)

cuidad_nombre_mas_largo = max (diccionario ["Ciudad"].values(),key=len)
cuidad_nombre_mas_corto = min (diccionario ["Ciudad"].values(),key=len)
print ("\n\nla cuidad con el nombre mas largo es {} y la cuidad con el nombre mas corto es {}".format (cuidad_nombre_mas_largo,cuidad_nombre_mas_corto))

mayor_monto_de_ganancias = max (diccionario ["Ganancias"].values())
mayor_monto_de_perdidad = max (diccionario ["Perdidas"].values())
print ("\n\nel mayor monto de ganancias es {} y el mayor monto de perdidad es {}".format (mayor_monto_de_ganancias,mayor_monto_de_perdidad))