"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar tipo de ordenamiento")
    print("3- Prueba ordenamiento")
    print("4- Mostrar obras de artista según tecnica")
    print("5- Mostrar obras según nacionalidad")
    print("6- Calcular costo de transporte de obras según departamento")
    print("7- Mostrar nueva exposición")
    print("0- Salir")


def initCatalog(tipo_lista):
    """
    Inicializa el catalogo de obras y artistas 
    """
    return controller.initCatalog(tipo_lista)

def loadData(catalog):
    """""
    Carga obras en la estructura de datos
    """
    controller.loadData(catalog)


catalog = None

typesort = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo_lista = int(input('Seleccione tipo de lista: \n 1. ARRAY_LIST \n 2. LINKED_LIST \n tipo de lista: '))
        print("Cargando información de los archivos ....\n")
        catalog = initCatalog(tipo_lista)
        loadData(catalog)
        sizeArtist = lt.size(catalog['artists'])
        sizeArtworks = lt.size(catalog['artworks'])

        print('Artistas cargados: ' + str(sizeArtist) + '\n')
    

        print('Obras cargadas: ' + str(sizeArtworks) + '\n')




    elif int(inputs[0]) == 2:
        
        #tipo de sort

        typeint = int(input("Tipo de sort a utilizar: \n 1. Insertion \n 2. Shell \n 3. Merge \n 4. Quick Sort \n tipo de sort:"))
        
        if typeint == 1:
            typesort = 1
        elif typeint ==2:
            typesort = 2
        elif typeint ==3:
            typesort = 3
        elif typeint ==4:
            typesort = 4


    elif int(inputs[0]) == 3:

        #longitud sub-lista

        size = input("tamaño de muestra a ordenar: ")

        if int(size) > lt.size(catalog['artworks']):
            size =  lt.size(catalog['artworks'])

        result = controller.sortArtworks(catalog, int(size),typesort)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))



    elif int(inputs[0]) == 4:
        nombre_artista = input("Nombre del artista: ")
        print("...")
        pass

    elif int(inputs[0]) == 5:
        print("...")
        pass

    elif int(inputs[0]) == 6:
        departamento = input("Departamento: ")
        print("...")
        pass

    elif int(inputs[0]) == 7:
        a_inicial = input("Año inicial de las obras: ")
        a_final = input("Año final de las obras: ")
        area = input("Area disponible para nueva exposicón: ")
        print("...")
        pass

    else:
        sys.exit(0)
sys.exit(0)
