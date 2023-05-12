'''
Debes realizar un menú que permita al usuario trabajar con las siguientes opciones:
1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
un personaje puede tener más de una raza y más de una habilidad.
2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
corresponden a esa raza.
3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
repetirse en los distintos listados.
4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
el nombre del perdedor. Este archivo anexará cada dato.
6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
Nombre del archivo:
Saiyan_Genki_Dama.Json
Datos :
Goten - 3000 - Kamehameha + Tambor del trueno
Goku - 5000000 - Kamehameha + Super Saiyan 2
7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción
6.
8. Salir del programa.
'''
import re
def parse_csv(path:str)->list:
    lista_personajes = []
    archivo = open(path, "r",encoding = "utf-8")
    for linea in archivo:
        lectura = re.split(",", linea)
        personajes = {}
        personajes["id"] = lectura[0]
        personajes["Nombre"] = lectura[1]
        personajes["Raza"] = lectura[2]
        personajes["Poder de pelea"] = int(lectura[3])
        personajes["Poder de ataque"] = int(lectura[4])
        personajes["Habilidades"] = parse_habilidades(lectura[5])
        lista_personajes.append(personajes)
    archivo.close()
    return lista_personajes

def parse_habilidades(habilidades:str):
        habilidades = habilidades.split("|$%")
        habilidades[-1] = habilidades[-1].replace("\n","")
        for habilidad in habilidades:
            habilidad = habilidad.rstrip()
        return habilidades

# def parse_raza(raza:str):
#     raza = raza.split("-")
#     return raza

def mostrar_lista(path):
    lista_personajes = parse_csv(path)
    print(lista_personajes)

lista_personajes = parse_csv("DBZ.csv")


'''2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
corresponden a esa raza.
'''
def contar_raza(lista:str):
    razas = {}
    for personaje in lista:
        for raza in personaje["Raza"]:
            if raza in razas:
                razas["Raza"] += 1
        else:
            razas["Raza"] = 1

    print("Cantidad de personajes por raza:")
    for raza, cantidad in razas.items():
        print(f"{raza}: {cantidad}")




'''
3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
repetirse en los distintos listados.
'''
def listar_raza(lista:list,clave:str)->None:
    lista_por_raza= []
    for personaje in lista:
        raza = personaje[clave]
        lista_por_raza.append(raza)
    
    lista_por_raza = set(lista_por_raza)
    
    for raza in lista_por_raza:
        print(raza)
        for personaje in lista:
            if personaje[clave] == raza:
                print(f'\t{personaje["Nombre"]}-{personaje["Poder de ataque"]}')

'''
4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
'''

def ingresar_habilidad():
    habilidad_ingresada = input("ingresa una habilidad de un personaje")
    return habilidad_ingresada

def promedio(lista:list,clave:str,clavedos:str)->int:
    habilidad_ingresada = ingresar_habilidad()
    for personajes in lista:
        if habilidad_ingresada == personajes["Habilidades"]:
            promedio = personajes[clave]+personajes[clavedos]/2
            print(promedio)

# def mostrar_personaje(lista:list):
#     habilidad = ingresar_habilidad()
#     for personajes in lista:
#         if personajes["Habilidades"] == habilidad :
#             print(f'{personajes["Nombre"]},{personajes["Raza"]},')






menu = ["1.Traer datos desde archivo", "2.Listar cantidad por raza","3.Listar personajes por raza",
        "4.Listar personajes por habilidad","5.Jugar batalla","6.Guardar Json",
        "7.Leer Json","8.Salir"]

def mostrar_opciones():
    for opcion in menu:
        print(opcion)

while True:
    
    mostrar_opciones()
    respuesta = int(input("ingrese una opcion: "))

    match respuesta:
        case 1:
            mostrar_lista("DBZ.csv")
        case 2: 
            contar_raza(lista_personajes)
        case 3: 
            listar_raza(lista_personajes,"Raza")
        case 4:
            promedio(lista_personajes,"Poder de pelea","Poder de ataque")
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            break