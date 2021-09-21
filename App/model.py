"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo_lista):
    """
    Inicializa el catálogo de obrs y artistar. Crea una lista vacia para guardar
    todos  Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    if tipo_lista == 1:
        catalog['artists'] = lt.newList('ARRAY_LIST')
        catalog['artworks'] = lt.newList('ARRAY_LIST')
    elif tipo_lista ==2:
        catalog['artists'] = lt.newList('LINKED_LIST')
        catalog['artworks'] = lt.newList('LINKED_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)
   
def addArtwork(catalog, artwork):
    # Se agrega una obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creacion de datos

# Funciones de consulta

def getArtistsInDateRange (catalog, year1, year2):
    """"
    Retorna lista desordenada de artistas en un rango de años
    """
    artists = catalog["artists"]
    artistsInRange= lt.newList(datastructure= "ARRAY_LIST")
    for artist in lt.iterator(artists):
        if int(artist["BeginDate"]) >= year1 and int(artist["BeginDate"]) <= year2:
            lt.addLast(artistsInRange, artist)
    return artistsInRange

def getArtworksInDateRange (catalog, year1, year2):
    """"
    Retorna lista desordenada de artworks en un rango de fechas utilizando el comparador cmpArtwork
    """
    artworks = catalog["artworks"]
    artworksInRange= lt.newList(datastructure= "ARRAY_LIST")
    for artwork in lt.iterator(artworks):
        if (cmpArtworkByDateAcquired(artwork,year2)) and not (cmpArtworkByDateAcquired(artwork, year1)):
            lt.addLast(artworksInRange, artwork)
    return artworksInRange

def purchasedAmount (artworksInRange):

    k = 0
    t = "purchase"
    for artwork in lt.iterator(artworksInRange):
       posible = artwork["CreditLine"].lower()
       if t in posible:
           k+=1
    return k

def searchArtistByID(catalog, constituentids):

    artists = catalog['artists']
    ID_list = constituentids.strip("[]").split(", ")
    artists_names=lt.newList('ARRAY_LIST')
    for id in ID_list:
        corte = 0
        while corte == 0:
            for artist in lt.iterator(artists):
                if artist["ConstituentID"] == id:
                    lt.addLast(artists_names,artist['DisplayName'])
                    corte = 1

    return artists_names


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtistsByBeginDate (artist1, artist2):

    result = int(artist1["BeginDate"]) < int(artist2["BeginDate"])
    return result

def cmpArtworkByDateAcquired(artwork1 , artwork2):

    # Devuelve True si el 'DateAcquired' de artwork1 es menor que el de artwork2

    date1 = artwork1['DateAcquired'].split('-')
    date2 = artwork2['DateAcquired'].split('-')

    if date1 == [""]:
        date1=["0000","00","00"]
    if date2 == [""]:
        date2=["0000","00","00"]

    resultado = True

    if date1[0] > date2[0]:
        resultado = False
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            resultado = False
        elif date1[1] == date2[1]:
            if date1[2] > date2[2]:
                resultado = False
    
    return(resultado)


# Funciones de ordenamiento

def sortArtists (artistsInRange):
    sub_list = lt.subList(artistsInRange, 1, lt.size(artistsInRange))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = ms.sort(sub_list, cmpArtistsByBeginDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list



def sortArtworks(artworksInRange):
    sub_list = lt.subList(artworksInRange, 1, lt.size(artworksInRange))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


