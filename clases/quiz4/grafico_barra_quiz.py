import matplotlib.pyplot as plt
import pandas as p 
barrios = p.read_csv("barrio.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)

plt.bar (barrios ["Barrio"].values(),barrios ["Agua"].values())
plt.title("GRAFICO DE BARRAS MEDELLÍN")
plt.xlabel("Barrios")
plt.ylabel("Agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("Barrios1.png")
#plt.close
plt.show()

plt.bar (barrios ["Barrio"].values(),barrios ["Gas"].values())
plt.title("GRAFICO DE BARRAS MEDELLÍN ")
plt.xlabel("Barrios")
plt.ylabel("Gas")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("Barrios2.png")
#plt.close
plt.show()

#electrocardiograma
ecg =p.read_csv("ecg_taller.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_primer_ecg.png")
#plt.close
plt.show()

# grafico de pie

labels = 'Bogota', 'Medellin', 'Leticia', 'villavicencio'
sizes = [80,7,5,8]
explode = [0,0,0.2,0]
plt.pie (sizes, explode=explode, labels=labels , shadow=True, startangle=45 )
plt.title ("Crisis del COVID-19")
plt.savefig ("Grafico_pie_covid.png")
plt.show()