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

##################################
#json de compras#

def abierto():
    jeisiton=[]
    with open('./compras.json','r') as openfile:
        jeisiton= json.load(openfile)
    return jeisiton

def archivoguardado(miData):
    with open("./compras.json","w") as outfile:
        json.dump(miData,outfile)

#######################################
#json de ventas

def inaugurado():
    jisiton2=[]
    with open('./ventas.json','r') as openfile:
        jisiton2= json.load(openfile)
    return jisiton2

def guardado2(miData):
    with open("./ventas.json","w") as outfile:
        json.dump(miData,outfile)


print("---------------------¬")
print("BIENVENIDO A PANCAMP")
print("----------------------")
print("")
print("1. ver reportes")
print("2. realizar una compra")
print("3. realizar una venta")
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
        print("2. stock")
        quereporte=input("")
        if quereporte=="1":
            jsoon=inaugurado()
            print("-----------------")
            print("Reporte de ventas")
            print("-----------------")
            for i in jsoon:
                contador=0
                print("|ID: ",i["id"])
                print("|NOMBRE CLIENTE: ",i["nombre"])
                print("|FECHA DE VENTA: ",i["fecha"])
                print("|PRODUCTO: ",i["producto"])
                print("|CANTIDAD: ",i["cantidad"])
                print("|PRECIO: ",i["precio"])
                ciclo=False
        if quereporte=="2":
            jsoonStock=abrirArchivo()
            print("-----------------")
            print("Reporte de stock")
            print("-----------------")
            for i in jsoonStock["Panaderia"]:
                contador=0
                print("------------------")
                print("stock de panaderia")
                print("------------------")
                print("|NOMBRE: ",i["producto"])
                print("|CANTIDAD: ",i["cantidad"])
                print("|PRECIO :",i["precio"])
                print("")
            for i in jsoonStock["Pasteleria"]:
                contador=0
                print("------------------")
                print("stock de Pasteleria")
                print("------------------")
                print("|NOMBRE: ",i["producto"])
                print("|CANTIDAD: ",i["cantidad"])
                print("|PRECIO :",i["precio"])
                print("")
            for i in jsoonStock["Bebidas"]:
                contador=0
                print("------------------")
                print("stock de Bebidas")
                print("------------------")
                print("|NOMBRE: ",i["producto"])
                print("|CANTIDAD: ",i["cantidad"])
                print("|PRECIO :",i["precio"])
                print("")
            for i in jsoonStock["Apartado de promociones"]:
                contador=0
                print("------------------")
                print("stock de Apartado de promociones")
                print("------------------")
                print("|NOMBRE: ",i["producto"])
                print("|CANTIDAD: ",i["cantidad"])
                print("|PRECIO :",i["precio"])
                print("")
    if opcion=="2":
        print("----------------------------------")
        print("BIENVENIDO A LA SECCION DE COMPRAS")
        print("----------------------------------")
        print("")
        jsoonCompras=abierto()
        print("LISTA DE PROOVEDORES")
        print("1 -julio cesar")
        print("2 -jhon alexander")
        print("3 -danna gomez")
        print("4 -franklin leonardo")
        print("5 -sebastain juan")
        print("")
        print("ingresa el id de proovedor que eres")
        queProovedor=int(input("¿Que proovedor eres? :"))
        queProducto=(input("¿Que producto se va a comprar? :"))
        jsoonCompras[queProovedor-1]["producto"]=queProducto
        archivoguardado(jsoonCompras)

        queCantidad=input("¿Que cantidad se va a comprar?: ")
        jsoonCompras[queProovedor-1]["cantidad"]=queProducto
        archivoguardado(jsoonCompras)

        quePrecio=input("¿Que precio tiene la compra?: ")
        jsoonCompras[queProovedor-1]["precio"]=queProducto
        archivoguardado(jsoonCompras)

        print("ahora dame tu informacion")
        queNombre=input("cual es tu nombre: ")
        jsoonCompras[queProovedor-1]["nombre"]=queProducto
        archivoguardado(jsoonCompras)

        queContacto=input("cual es tu numero de contacto: ")
        jsoonCompras[queProovedor-1]["contacto"]=queProducto
        archivoguardado(jsoonCompras)

        queFecha=input("en que fecha se va a realizar la compra: ")
        jsoonCompras[queProovedor-1]["fecha"]=queProducto
        archivoguardado(jsoonCompras)
        ciclo=False

    if opcion=="3":
        print("----------------------------------")
        print("BIENVENIDO A LA SECCION DE VENTAS")
        print("----------------------------------")
        print("")
        jsoonVentas=inaugurado()
        queVenta=int(input("en la factura de la venta entre el 1 y el 5 que id se te dio: "))
        queFecha2=input("en que fecha se realizo la venta: ")
        jsoonVentas[queVenta-1]["fecha"]=queFecha2
        guardado2(jsoonVentas)

        queNombre2=input("cual es tu nombre: ")
        jsoonVentas[queVenta-1]["nombre"]=queNombre2
        guardado2(jsoonVentas)

        queDireccion2=input("cual es tu direccion: ")
        jsoonVentas[queVenta-1]["direccion"]=queDireccion2
        guardado2(jsoonVentas)
        
        queEmpleado2=input("cual es el nombre del empleado: ")
        jsoonVentas[queVenta-1]["empleado"]=queEmpleado2
        guardado2(jsoonVentas)

        queCargo2=input("cual es el cargo que tiene: ")
        jsoonVentas[queVenta-1]["cargo"]=queCargo2
        guardado2(jsoonVentas)

        queProducto2=input("cual es el producto: ")
        jsoonVentas[queVenta-1]["producto"]=queProducto2
        guardado2(jsoonVentas)

        queCantidad2=input("cual es la cantidad: ")
        jsoonVentas[queVenta-1]["cantidad"]=queCantidad2
        guardado2(jsoonVentas)

        quePrecio2=input("cual es el precio: ")
        jsoonVentas[queVenta-1]["precio"]=quePrecio2
        guardado2(jsoonVentas)
        ciclo=False

        







