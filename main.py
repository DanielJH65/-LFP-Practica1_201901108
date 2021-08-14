from tkinter import Tk
from tkinter.filedialog import askopenfilename
import webbrowser

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

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

def separarAlumnos(datos):
    alumnos1 = []
    for i in datos:
        i = i.replace("<","")
        i = i.replace(">","")
        i = i.replace(",","")
        i = i.replace('"',"")
        alumnos1.append(separarDatos(i,";"))
    return alumnos1

def crearObjetos(alumnos1):
    listafinal = []
    for temp in alumnos1:
        alumno = Alumno(temp[0], int(temp[1]))
        listafinal.append(alumno)
    return listafinal

def salidaConsola(curso, alumnos, parametros):
    pass

if __name__ == '__main__':
    opcion = 0
    curso = ""
    curso = ""
    parametros = []
    alumnosFinal = []
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
            longitud = len(separados1)
            parametro = separados1[longitud-1].replace("}","")
            parametros = separarDatos(parametro,",")
            separados1.pop(longitud-1)
            alumnos1 = separarAlumnos(separados1)
            alumnosFinal = crearObjetos(alumnos1)
        elif opcion == 2:
            salidaConsola(curso, alumnosFinal, parametros)
        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("\nDebe ingresar un número valido")