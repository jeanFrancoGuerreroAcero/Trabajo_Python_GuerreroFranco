import json

with open("./info.json", encoding= "utf-8") as file:
    mijson= json.load(file)

def abrirArchivo():
    miJSON=[]
    with open('./info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("./info.json","w") as outfile:
        json.dump(miData,outfile)

print("---------------------¬")
print("BIENVENIDO A PANCAMP")
print("----------------------")
print("")
print("1. ver reportes")
print("2. realizar una compra")
print("")
opcion=input("¿Que opcion deseas realizar?: ")
ciclo=True

while ciclo:
    if opcion=="1":
        jsoon=abrirArchivo()
        print("----------------------------------------------")
        print("bienvenido a la seccion de reportes de pancamp")
        print("----------------------------------------------")
        print("")
        print("Que reporte desea visualizar")
        print("1. ventas")
        print("2. compras")
        quereporte=input("")
        if quereporte=="1":
            jsoon=abrirArchivo()
            print("-----------------")
            print("Reporte de ventas")
            print("-----------------")
            for i in jsoon ["Panaderia"]:
                contador=0
                print("|ID: ",i)
                print("|NOMBRE: ",i)
                print("|FECHA DE VENTA: ",i)
                print("|")
    

                ciclo=False






