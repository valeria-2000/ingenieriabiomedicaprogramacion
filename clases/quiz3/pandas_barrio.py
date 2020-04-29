import pandas as p 
diccionario = p.read_csv("barrio.csv",encoding='UTF-8',header = 0 ,delimiter=';').to_dict()
print (diccionario)

barrio_nombre_largo = max (diccionario ["Barrio"].values(),key=len)
barrio_nombre_corto = min (diccionario ["Barrio"].values(),key=len)
print ("\n\n El barrio con el nombre más largo es {} y el barrio con el nombre más corto es {}".format (barrio_nombre_largo,barrio_nombre_corto))

consumo_minimo_agua = min (diccionario ["Agua"].values())
consumo_maximo_agua = max (diccionario ["Agua"].values())
print ("\n\n El consumo  mínimo de agua es {} y el consumo máximo de agua es {} ".format (consumo_minimo_agua,consumo_maximo_agua))
consumo_minimo_energia = min (diccionario ["Energía"].values())
consumo_maximo_energia = max (diccionario ["Energía"].values())
print ("\n\n El consumo  mínimo de energía es {} y el consumo máximo de energía es {} ".format (consumo_minimo_energia,consumo_maximo_energia))
consumo_minimo_gas = min (diccionario ["Gas"].values())
consumo_maximo_gas = max (diccionario ["Gas"].values())
print ("\n\n El consumo  mínimo de gas es {} y el consumo máximo de gas es {} ".format (consumo_minimo_gas,consumo_maximo_gas))
consumo_minimo_internet = min (diccionario ["Internet"].values())
consumo_maximo_internet = max (diccionario ["Internet"].values())
print ("\n\n El consumo  mínimo de internet es {} y el consumo máximo de internet es {} ".format (consumo_minimo_internet,consumo_maximo_internet))

cantidad_maxima_habitantes = max (diccionario ["Habitantes"].values())
cantidad_minima_habitantes = min (diccionario ["Habitantes"].values())
print("\n\n La cantidad máxima de habitantes es {} y la cantidad mínima de habitantes es {} ".format (cantidad_maxima_habitantes,cantidad_minima_habitantes))