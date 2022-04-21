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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def inicializarAnalizer():
    analizer={}
    analizer['listaPlayers']=lt.newList('SINGLE_LINKED', compareIds)
    analizer['playerClubName'] =mp.newMap(184,
                        maptype='PROBING',
                        loadfactor=0.5)

    return analizer

def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def addPlayerLista(analizer, player):
    listaJugadores=analizer['listaPlayers']
    lt.addLast(listaJugadores, player)
    return(listaJugadores)

def addPlayerClubName(analizer, player):
    clubName=player['club_name']
    if mp.contains(analizer['playerClubName'], clubName) ==False:
        listaPlayers=lt.newList('ARRAY_LIST')
        lt.addLast(listaPlayers, player)
        mp.put(analizer['playerClubName'], clubName, listaPlayers )
    else:
        llaveValor=mp.get(analizer['playerClubName'], clubName)
        listaPlayers=me.getValue(llaveValor)
        lt.addLast(listaPlayers, player)

def mapPlayerClubDate(analizer, clubName):
    playerClubDate=om.newMap(omaptype='RBT',
                            comparefunction=compareDates)
    llaveValor=mp.get(analizer['playerClubName'], clubName)
    listaPlayers=me.getValue(llaveValor)
    for player in lt.iterator(listaPlayers):
        date=player['club_joined']
        date= datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
        if mp.contains(playerClubDate, date) ==False:
            listaPlayers=lt.newList('ARRAY_LIST')
            lt.addLast(listaPlayers, player)
            mp.put(playerClubDate, clubName, listaPlayers )
        else:
            llaveValor=mp.get(playerClubDate, date)
            listaPlayers=me.getValue(llaveValor)
            lt.addLast(listaPlayers, player)

    return playerClubDate
    


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1