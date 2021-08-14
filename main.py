from tkinter import Tk
from tkinter.filedialog import askopenfilename
import webbrowser

if __name__ == "__main__":
    opcion = 0
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
            Tk().withdraw()
            archivo = askopenfilename()
            archivo = open(archivo, "r")
            datos = archivo.read()
            archivo.close()
            separar_datos(datos, "\n")
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("\nDebe ingresar un número valido")

def separar_datos(datos, separador):
    temp = ""