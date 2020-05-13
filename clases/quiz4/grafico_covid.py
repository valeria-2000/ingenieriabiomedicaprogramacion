import matplotlib.pyplot as plt
import pandas as p 
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)


plt.bar (inventario ["Elemento"].values(),inventario ["Unidade "].values(), color = "r", alpha = 0.2)
plt.title("GRAFICO DE BARRAS COVID-19")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("elementoVSunidades.png")
plt.close
plt.show()


plt.bar (inventario ["Elemento"].values(),inventario ["Viejo "].values(), color = "r", alpha = 0.6)
plt.title("GRAFICO DE BARRAS COVID-19")
plt.xlabel("Elemento")
plt.ylabel("Elementos viejos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("elementosVSviejos.png")
plt.close
plt.show()


plt.bar (inventario ["Elemento"].values(),inventario ["Nuevos"].values(), color = "r")
plt.title("GRAFICO DE BARRAS COVID-19")
plt.xlabel("Elemento")
plt.ylabel("Nuevos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("elementosVSnuevos.png")
plt.close
plt.show()

#Fotopletismografía
ecg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("PPG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_primer_ppg.png")
plt.close
plt.show()

print ("En la fotopletismografia veo 9 picos")

#Grafico de Pie

labels = 'Recuperandose en Casa', 'Hospitalizados', 'UCI'
sizes = [85,10,5]
explode = [0,0,0.2]
plt.pie (sizes, explode=explode, labels=labels , shadow=True, startangle=45 ,)
plt.title ("Crisis del COVID-19")
plt.savefig ("Grafico_pie_Hopital.png")
plt.close
plt.show()