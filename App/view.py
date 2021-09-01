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
    print("2- Mostrar lista de artistas de una época")
    print("3- Mostrar lista de adquisiciones de una época")
    print("4- Mostrar obras de artista según tecnica")
    print("5- Mostrar obras según nacionalidad")
    print("6- Calcular costo de transporte de obras según departamento")
    print("7- Mostrar nueva exposición")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de obras y artistas 
    """
    return controller.initCatalog()

def loadData(catalog):
    """""
    Carga obras en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....\n")
        catalog = initCatalog()
        loadData(catalog)
        sizeArtist = lt.size(catalog['artists'])
        sizeArtworks = lt.size(catalog['artworks'])

        print('Artistas cargados: ' + str(sizeArtist) + '\n')
        print( str(lt.getElement(catalog["artists"],sizeArtist-2)) + '\n' 
        + str(lt.getElement(catalog["artists"],sizeArtist-1)) + '\n'
        +str(lt.getElement(catalog["artists"],sizeArtist))+ '\n')

        print('Obras cargadas: ' + str(sizeArtworks) + '\n')
        print( str(lt.getElement(catalog["artworks"],sizeArtworks-2)) + '\n' 
        + str(lt.getElement(catalog["artworks"],sizeArtworks-1)) + '\n'
        +str(lt.getElement(catalog["artworks"],sizeArtworks))+ '\n')



    elif int(inputs[0]) == 2:
        a_inicial = input("Año inicial: ")
        a_final = input("Año final: ")
        print("...")
        pass

    elif int(inputs[0]) == 3:
        f_inicial = input("Fecha inicial (AAAA-MM-DD): ")
        f_final = input("Fecha final (AAAA-MM-DD): ")
        print("...")
        pass

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
