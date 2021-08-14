from tkinter import Tk
from tkinter.filedialog import askopenfilename
import webbrowser

def abrirArchivo():
    Tk().withdraw()
    archivo = askopenfilename()
    archivo = open(archivo, "r")
    datos = archivo.read()
    archivo.close()
    return datos

def separarDatos(datos, separador):
    temp = ""
    listaTemp = []

    for char in  datos:
        if char == separador:
            listaTemp.append(temp.strip())
            temp = ""
        else:
            temp += char
    if temp.strip() != "":
        listaTemp.append(temp.strip())
    return listaTemp

if __name__ == '__main__':
    opcion = 0
    curso = ""
    while(opcion != 4):
        opcion = int(input("""
###############--Menú--###############
#                                    #
#   Elija una opción:                #
#   1) Cargar archivo de entrada     #
#   2) Mostrar Reporte en Consola    #
#   3) Exportar Reporte              #
#   4) Salir                         #
#                                    # 
######################################  
    """))
        if opcion == 1:
            datos = abrirArchivo()
            separados1 = separarDatos(datos, "\n")
            curso = separados1[0].replace("{","")
            curso = curso.replace("=","")
            separados1.pop(0)
            print(curso)
            print(separados1)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("\nDebe ingresar un número valido")