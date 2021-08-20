from tkinter import Tk
from tkinter.filedialog import askopenfilename
import webbrowser
html = ""
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

def burbujaAsc(alumnos):
    tamano = len(alumnos)-1
    i = 0
    for i in range(tamano):
        j = 0
        for j in range(tamano):
            if alumnos[j].nota > alumnos[j+1].nota:
                alumnos[j+1], alumnos[j]= alumnos[j],alumnos[j+1]

def burbujaDesc(alumnos):
    i = 0
    for i in range(len(alumnos) - 1):
        j = 0
        for j in range(len(alumnos) - 1):
            if alumnos[j].nota < alumnos[j+1].nota:
                alumnos[j+1], alumnos[j]= alumnos[j],alumnos[j+1]

def salidaConsola(curso, alumnos, parametros,html):
    largo = len(alumnos)
    print('''
================================================
> Curso : {0}
> Total de estudiante: {1}

>Listado desordenado
'''.format(curso, largo))
    html+="""<br><center><h2>{0}</h2></center><br>
    <center><h2>Número de estudiantes: {1}</h2></center><br>""".format(curso, largo)
    html+="""
    <div class="jumbotron mx-4">
            <br><center><h3>Listado Desordenado</h3></center><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Nota</th>
                    </tr>
                </thead>
                <tbody>
    """
    for k in alumnos:
        print(">> Nombre:", k.nombre, "\nNota: ", k.nota)
        if k.nota >= 61:
            html+='<tr class="table-info">'
        else:
            html+='<tr class="table-danger">'
        html+="""
                <th scope="row">{0}</th>
                <td>{1}</td>
            </tr>
        """.format(k.nombre,k.nota)
    print("")
    html+="""
                </tbody>
            </table>
            </div>
            """
    aprobados = 0
    reprobados = 0
    sum = 0
    maxi = 0
    mini = alumnos[0].nota
    for i in alumnos:
        nota = i.nota
        sum+= nota
        if nota >= 61:
            aprobados += 1
        else:
            reprobados += 1
        if nota > maxi:
            maxi = nota
        if nota < mini:
            mini = nota
    promedio = sum/largo

    
    for i in parametros:
        if i == "ASC":
            print("> Listado ordenado Ascendete:\n")
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>Listado ordenado Ascendete</h3></center><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Nota</th>
                    </tr>
                </thead>
                <tbody>
            """
            asc = alumnos
            burbujaAsc(asc)
            for j in asc:
                print(">> Nombre:", j.nombre, "\nNota: ", j.nota)
                if j.nota >= 61:
                    html+='<tr class="table-info">'
                else:
                    html+='<tr class="table-danger">'
                html+="""
                        <th scope="row">{0}</th>
                        <td>{1}</td>
                    </tr>
                """.format(j.nombre,j.nota)
            print("")
            html+="""
                </tbody>
            </table>
            </div>
            """
        elif i == "DESC":
            print("> Listado ordenado Descendete:\n")
            desc = alumnos
            burbujaDesc(desc)
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>Listado ordenado Ascendete</h3></center><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Nota</th>
                    </tr>
                </thead>
                <tbody>
            """
            for j in desc:
                print(">> Nombre:", j.nombre, "\nNota:", j.nota)
                if j.nota >= 61:
                    html+='<tr class="table-info">'
                else:
                    html+='<tr class="table-danger">'
                html+="""
                        <th scope="row">{0}</th>
                        <td>{1}</td>
                    </tr>
                """.format(j.nombre,j.nota)
            print("")
            html+="""
                </tbody>
            </table>
            </div>
            """
        elif i == "AVG":
            print("> El promedio de los estudiantes es: {:.2f}\n".format(promedio))
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>El promedio de los estudiantes es: {:.2f}</h3></center><br>
            </div>
            """.format(promedio)
        elif i == "MIN":
            print("> La nota mínima es de: {0}\n".format(mini))
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>La nota mínima es de: {0}</h3></center><br>
            </div>
            """.format(mini)
        elif i == "MAX":
            print("> La nota máxima es de: {0}\n".format(maxi))
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>La nota máxima es de: {0}</h3></center><br>
            </div>
            """.format(maxi)
        elif i == "APR":
            print("> El número de estudiantes aprobados es: {0}\n".format(aprobados))
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>El número de estudiantes aprobados es: {0}</h3></center><br>
            </div>
            """.format(reprobados)
        elif i == "REP":
            print("> El número de estudiantes reprobados es: {0}\n".format(reprobados))
            html+="""
            <div class="jumbotron mx-4">
            <br><center><h3>El número de estudiantes reprobados es: {0}</h3></center><br>
            </div>
            """.format(aprobados)
        else:
            print("Parametros no validos")
    print("================================================")
    return html

def generarHtml(html):
    pagina = open('Reporte Alumnos.html', 'w')
    salida = """<!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://bootswatch.com/4/superhero/bootstrap.min.css" rel="stylesheet" type="text/css">
    <title>Alumnos</title>
    </head>
    <body style="background: linear-gradient(to right, #141e30, #243b55);">
    <nav class="navbar navbar-expand-lg navbar-dark bg-secondary">
        <a class="navbar-brand" href="#">Practica LFPB+</a>
        <a class="navbar-brand" href="#">Walter Daniel Jimenez Hernandez 201901108</a>
    </nav>
    """
    salida+=html
    salida += """</body>
    </html>
    """
    pagina.write(salida)
    pagina.close()
    webbrowser.open_new_tab('Reporte Alumnos.html')

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
            html+= salidaConsola(curso, alumnosFinal, parametros, html)
        elif opcion == 3:
            generarHtml(html)
        elif opcion == 4:
            break
        else:
            print("\nDebe ingresar un número valido")