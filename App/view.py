﻿"""
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

import sys
...
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar artistas en un rango de fechas")
    print("3- Listar adquisiciones en un rango de fechas")
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


def printArtworksSortResults(ord_artworks):

    cantidad = lt.size(ord_artworks)
    print('\nSe encontraron ' + str(cantidad) + ' obras en el rango ingresado')

    
    print("\nLas primeras 3 obras en el rango son: ")

    i=1
    while i in range(1,4):
        artwork = lt.getElement(ord_artworks,i)
        constituents = artwork["ConstituentID"]
        artistas = controller.searchArtistByID(catalog, constituents)
        cantidad_artistas = lt.size(artistas)
        
        print('\nTitulo: ' + artwork['Title'] + ' \n\nArtistas: ')

        for num in range(0,cantidad_artistas):
            artista = lt.getElement(artistas, num + 1)
            print(str(artista))
        
        print('\nFecha: ' + artwork['Date'] +
           ', Fecha adquisición: ' + artwork['DateAcquired'] +
            ', Medio: ' + artwork['Medium'] +
            ' , Dimensiones: ' + artwork['Dimensions'] )
        i+=1
    
    print("\nLas últimas 3 obras en el rango son: ")

    k=2
    while k in range(0,3):
        pos = int(lt.size(ord_artworks))- k
        artwork = lt.getElement(ord_artworks,pos)

        constituents = artwork["ConstituentID"]
        artistas = controller.searchArtistByID(catalog, constituents)
        cantidad_artistas = lt.size(artistas)
        
        print('\nTitulo: ' + artwork['Title'] + ' \n\nArtistas: ')

        for num in range(0,cantidad_artistas):
            artista = lt.getElement(artistas, num + 1)
            print(str(artista))
        
        print('\nFecha: ' + artwork['Date'] +
           ', Fecha adquisición: ' + artwork['DateAcquired'] +
            ', Medio: ' + artwork['Medium'] +
            ' , Dimensiones: ' + artwork['Dimensions'] )
        
        k-=1

def printArtistSortResults(ord_artists):

    cantidad = lt.size(ord_artists)
    print('\nSe encontraron ' + str(cantidad) + ' artistsas en el rango ingresado')
    
    print("\nLos primeros 3 artistas en el rango son: ")

    i=1
    while i in range(1,4):
        artist = lt.getElement(ord_artists,i)
        print('\nNombre: ' + artist['DisplayName'] +
         ', Año de nacimiento: ' + artist['BeginDate'] +
          ', Año de fallecimiento: ' + artist['EndDate'] +
           ', Nacionalidad: ' + artist['Nationality'] +
            ', Genero: ' + artist['Gender'] )
        i+=1

    print("\nLos ultimos 3 artistas en el rango son: ")

    k=2
    while k in range(0,3):
        pos = int(lt.size(ord_artists))- k
        artist = lt.getElement(ord_artists, pos)
        print('\nNombre: ' + artist['DisplayName'] +
         ', Año de nacimiento: ' + artist['BeginDate'] +
          ', Año de fallecimiento: ' + artist['EndDate'] +
           ', Nacionalidad: ' + artist['Nationality'] +
            ', Genero: ' + artist['Gender'] )
        k-=1

    
def printCountriesSortResult(ord_countries):

    print("\nLos 10 paises con mas obras en el MoMa son: ")

    for nationality in lt.iterator(ord_countries):
        print("\n" + nationality['name'] + " : " + str(nationality['size']))

    pais = lt.getElement(ord_countries, 1)
    print("las primeras y utlimas 3 obras de la lista de obras nacionalidad: " + pais["name"]+ ", son: ")
    obras = pais['artworks']
    size = pais['size']
    for pos in [1,2,3,size-2,size-1,size]:
        obra = lt.getElement(obras, pos)
        constituents = obra["ConstituentID"]
        artistas = controller.searchArtistByID(catalog, constituents)
        cantidad_artistas = lt.size(artistas)

        print('\n############\nTitulo: ' + obra['Title'] + ' \n\nArtistas: ')

        for num in range(0,cantidad_artistas):
            artista = lt.getElement(artistas, num + 1)
            print(str(artista))
        
        print('\nFecha: ' + obra['Date'] +
           ', Fecha adquisición: ' + obra['DateAcquired'] +
            ', Medio: ' + obra['Medium'] +
            ' , Dimensiones: ' + obra['Dimensions'] )


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo_lista = int(input('\nSeleccione tipo de lista: \n1. ARRAY_LIST \n2. LINKED_LIST \ntipo de lista: '))
        print("\nCargando información de los archivos ....\n")
        catalog = initCatalog(tipo_lista)
        loadData(catalog)
        sizeArtist = lt.size(catalog['artists'])
        sizeArtworks = lt.size(catalog['artworks'])

        print('Artistas cargados: ' + str(sizeArtist) + '\n')
    

        print('Obras cargadas: ' + str(sizeArtworks) + '\n')




    elif int(inputs[0]) == 2:
        
        fecha1 = int(input('Año inicial de busqueda: '))
        fecha2 = int(input('Año final de busqueda: '))
        size = lt.size(catalog['artists'])

        result = controller.sortArtistsByBeginDate(catalog, fecha1, fecha2)
        print("\nPara la muestra de", size, " artistas, el tiempo (mseg) es: ", str(result[0]))
        printArtistSortResults(result[1])

        



    elif int(inputs[0]) == 3:

        fecha1 = input('Fecha inicial de busqueda (AAAA-MM-DD): ')
        est_fecha1 = {'DateAcquired':fecha1}
        fecha2 = input('Fecha final de busqueda (AAAA-MM-DD): ')
        est_fecha2 = {'DateAcquired': fecha2}
        size = lt.size(catalog['artworks'])

        result = controller.sortArtworksByBeginDate(catalog, est_fecha1, est_fecha2)
        print("\nPara la muestra de", size, " obras, el tiempo (mseg) es: ", str(result[0][0]))
        print("\nSe encontraron " + str(result[1]) + " obras compradas en el rango")
        printArtworksSortResults(result[0][1])


    elif int(inputs[0]) == 4:
        nombre_artista = input("Nombre del artista: ")
        print("...")
        pass

    elif int(inputs[0]) == 5:
        
        size = lt.size(catalog['nationalities'])

        result = controller.sortCountries(catalog)
        print("\n Para una muestra de", size, "paises, el tiempo (mseg) es: ", str(result[0]))
        printCountriesSortResult(result[1])


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
