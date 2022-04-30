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
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#CARGA DE DATOS
def inicializarAnalizer():
    analizer={}
    analizer['jugadorSofifaId']=om.newMap(omaptype='RBT',
                             comparefunction=compareSofifaId)
    analizer['jugadorClub']=mp.newMap(185,
                            maptype='PROBING',
                             loadfactor=0.5)
    analizer['jugadorPosicion']=mp.newMap(185,
                            maptype='PROBING',
                             loadfactor=0.5)
    analizer['jugadorSalario']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion2)
    analizer["birthdayPlayer"] = om.newMap(omaptype='RBT', 
                            comparefunction=funcionComparacion2)
    analizer['jugadorOverall']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorPotencial']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorValor']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorSalario']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)                        
    analizer['jugadorEdad']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorEstatura']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorPeso']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    analizer['jugadorLiberar']=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    return analizer

def compareSofifaId(id1, id2):
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1

def addPlayerSofifaId(analizer, jugador):
    id=jugador['sofifa_id']
    listaSofifa=om.put(analizer['jugadorSofifaId'],id, jugador)
    return(listaSofifa)
    
#REQUERIMIENTO 1
def jugadoresClub(analizer, jugador):
    club=jugador['club_name']
    if mp.contains(analizer['jugadorClub'],club)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorClub'], club, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorClub'], club)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorClubFecha(analizer, nombreClub):
    llaveValor=mp.get(analizer['jugadorClub'], nombreClub)
    listaJugadores=me.getValue(llaveValor)
    listaJugadores=mer.sort(listaJugadores, compReq1)
    return listaJugadores

def compReq1(jugador1, jugador2):
    joined1=datetime.datetime.strptime(jugador1['club_joined'], '%Y-%m-%d')
    joined2=datetime.datetime.strptime(jugador2['club_joined'], '%Y-%m-%d')
    dob1=datetime.datetime.strptime(jugador1['dob'], '%Y-%m-%d')
    dob2=datetime.datetime.strptime(jugador2['dob'], '%Y-%m-%d')
    if joined1!=joined2:
        return joined1>joined2 
    else:
        if jugador1['age']!=jugador2['age']:
            return jugador1['age']>jugador2['age']
        else:
            if dob1!=dob2:
                return dob1>dob2
            else: 
                return jugador1['short_name']>jugador2['short_name']

#REQUERIMIRNTO2 2
def jugadoresPosicion(analizer, jugador):
    pos=str(jugador['player_positions'])
    pos=pos.replace(' ','')
    pos=pos.split(',')
    for posicion in pos:
        if mp.contains(analizer['jugadorPosicion'],posicion)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores,jugador)
            mp.put(analizer['jugadorPosicion'], posicion, listaJugadores)
        else:
            llaveValor=mp.get(analizer['jugadorPosicion'], posicion)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)

def jugadoresDesempenio(analizer, posicion, minOverall, maxOverall,minPotencial, maxPotencial, minSalario, maxSalario):
    llaveValor=mp.get(analizer['jugadorPosicion'],posicion)
    listaJugadores=me.getValue(llaveValor)
    mapaDesempenio=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    for jugador in lt.iterator(listaJugadores):
        desempenio=int(jugador['overall'])
        if om.contains(mapaDesempenio, desempenio)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores, jugador)
            om.put(mapaDesempenio, desempenio, listaJugadores)
        else:
            llaveValor=om.get(mapaDesempenio,desempenio)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)
    listaDesempenio=om.values(mapaDesempenio, minOverall, maxOverall)
    mapaPotencial=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    for lista in lt.iterator(listaDesempenio):
        for jugador in lt.iterator(lista):
            potencial=int(jugador['potential'])
            if mp.contains(mapaPotencial, potencial)==False:
                listaJugadores=lt.newList('ARRAY_LIST')
                lt.addLast(listaJugadores, jugador)
                om.put(mapaPotencial, potencial, listaJugadores)
            else:
                llaveValor=om.get(mapaPotencial,potencial)
                listaJugadores=me.getValue(llaveValor)
                lt.addLast(listaJugadores, jugador)
    listaPotencial=om.values(mapaPotencial, minPotencial, maxPotencial)
    mapaSalario=om.newMap(omaptype='RBT',
                             comparefunction=funcionComparacion)
    for lista in lt.iterator(listaPotencial):
        for jugador in lt.iterator(lista):
            salario=int(float(jugador['wage_eur']))
            if salario!='':
                if mp.contains(mapaSalario, salario)==False:
                    listaJugadores=lt.newList('ARRAY_LIST')
                    lt.addLast(listaJugadores, jugador)
                    om.put(mapaSalario, salario, listaJugadores)
                else:
                    llaveValor=om.get(mapaSalario,salario)
                    listaJugadores=me.getValue(llaveValor)
                    lt.addLast(listaJugadores, jugador)
            else:
                salario=-1
                if mp.contains(mapaSalario, salario)==False:
                    listaJugadores=lt.newList('ARRAY_LIST')
                    lt.addLast(listaJugadores, jugador)
                    om.put(mapaSalario, salario, listaJugadores)
                else:
                    llaveValor=om.get(mapaSalario,salario)
                    listaJugadores=me.getValue(llaveValor)
                    lt.addLast(listaJugadores, jugador)
    listasalario= om.values(mapaSalario, minSalario, maxSalario)
    listaJugadores=lt.newList('ARRAY_LIST')
    for lista in lt.iterator(listasalario):
        for jugador in lt.iterator(lista):
            lt.addLast(listaJugadores,jugador)
    listaJugadores=mer.sort(listaJugadores, compReq2)
    return listaJugadores

def compReq2(valor1, valor2):
    if valor2['overall']!= valor1['overall']:
        return int(valor2['overall'])<int(valor1['overall'])
    else:
        if valor1['potential']!= valor2['potential']:
            return int(valor2['potential'])< int(valor1['potential'])
        else:
            if float(valor2['wage_eur'])!= float(valor1['wage_eur']):
                return float(valor1['wage_eur']) < float(valor2['wage_eur'])
            else:
                if valor2['age']!= valor1['age']:
                    return int(valor1['age'])< int(valor2['age'])
                else:
                    return  valor1['short_name']< valor2['short_name']
    
#REQUERIMIENTO 3
def jugadorSalario(analizer, jugador):
    salario=int(float(jugador['wage_eur']))
    if mp.contains(analizer['jugadorSalario'],salario)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorSalario'], salario, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorSalario'], salario)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)
def jugadoresSalarioCaracteristica(analizer,minSalario, maxSalario, caracteristica):
    listaJugadores=lt.newList('ARRAY_LIST')
    jugadoresSalario=analizer['jugadorSalario']
    rangoSalario=om.values(jugadoresSalario, minSalario, maxSalario)
    for lista in lt.iterator(rangoSalario):
        for jugador in lt.iterator(lista):
            if caracteristica in jugador['player_tags']:
                lt.addLast(listaJugadores, jugador)
    listaJugadores=mer.sort(listaJugadores, compReq3)
    return listaJugadores

def compReq3(valor1, valor2):
    if float(valor2['wage_eur'])!=float(valor1['wage_eur']):
        return float(valor2['wage_eur'])<float(valor1['wage_eur'])
    else:
        if int(valor2['overall'])!= int(valor1['overall']):
            return int(valor2['overall'])<int(valor1['overall'])
        else:
            if int(valor1['potential'])!= int(valor2['potential']):
                return int(valor2['potential'])< int(valor1['potential'])
            else:
                return valor1['long_name']<valor2['long_name']

#REQUERIMIENTO 4
def addPlayerBirthday(analizer, player):
    playerBirthday=player["dob"]
    if om.contains(analizer["birthdayPlayer"], playerBirthday) == False:
        listaPlayers=lt.newList("ARRAY_LIST")
        lt.addLast(listaPlayers, player)
        om.put(analizer["birthdayPlayer"], playerBirthday, listaPlayers)
    else: 
        llaveValor=om.get(analizer['birthdayPlayer'], playerBirthday)
        listaPlayers=me.getValue(llaveValor)
        lt.addLast(listaPlayers, player)

def jugadorFechaNacimiento(analizer, fechaInicio, fechaFinal, caracteristica):
    listaFinal=lt.newList("ARRAY_LIST")
    listaDeListas= om.values(analizer["birthdayPlayer"], fechaFinal, fechaInicio)
    for listaJugadores in lt.iterator(listaDeListas):
        for jugador in lt.iterator(listaJugadores):
            if caracteristica in jugador["player_traits"]:
                lt.addLast(listaFinal, jugador)
    return listaFinal
                
#Funciones Comparacion
def funcionComparacion2(valor1, valor2):
    '''
    ordena de mayor a menor
    '''
    if (valor1 == valor2):
        return 0
    elif (valor1 < valor2):
        return 1
    else:
        return -1
def funcionComparacion(valor1, valor2):
    '''
    ordena de menor a mayor
    '''
    if (valor1 == valor2):
        return 0
    elif (valor1 > valor2):
        return 1
    else:
        return -1

#REQUERIMIENTO 5
def jugadorOverall(analizer, jugador):
    overall=int(jugador['overall'])
    if mp.contains(analizer['jugadorOverall'],overall)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorOverall'], overall, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorOverall'], overall)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorPotencial(analizer, jugador):
    potencial=int(jugador['potential'])
    if mp.contains(analizer['jugadorPotencial'],potencial)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorPotencial'], potencial, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorPotencial'], potencial)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorValor(analizer, jugador):
    if jugador['value_eur']!='':
        valor=int(float(jugador['value_eur']))
        if mp.contains(analizer['jugadorValor'],valor)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores,jugador)
            mp.put(analizer['jugadorValor'], valor, listaJugadores)
        else:
            llaveValor=mp.get(analizer['jugadorValor'], valor)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)
    else:
        valor=-1
        if mp.contains(analizer['jugadorValor'],valor)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores,jugador)
            mp.put(analizer['jugadorValor'], valor, listaJugadores)
        else:
            llaveValor=mp.get(analizer['jugadorValor'], valor)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)

def jugadorEdad(analizer, jugador):
    edad=int(jugador['age'])
    if mp.contains(analizer['jugadorEdad'],edad)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorEdad'], edad, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorEdad'], edad)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorEstatura(analizer, jugador):
    estatura=int(jugador['height_cm'])
    if mp.contains(analizer['jugadorEstatura'],estatura)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorEstatura'], estatura, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorEstatura'], estatura)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorPeso(analizer, jugador):
    peso=int(jugador['weight_kg'])
    if mp.contains(analizer['jugadorPeso'],peso)==False:
        listaJugadores=lt.newList('ARRAY_LIST')
        lt.addLast(listaJugadores,jugador)
        mp.put(analizer['jugadorPeso'], peso, listaJugadores)
    else:
        llaveValor=mp.get(analizer['jugadorPeso'], peso)
        listaJugadores=me.getValue(llaveValor)
        lt.addLast(listaJugadores, jugador)

def jugadorLiberar(analizer, jugador):
     if jugador['release_clause_eur']!='':
        liberar=int(float(jugador['release_clause_eur']))
        if mp.contains(analizer['jugadorLiberar'],liberar)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores,liberar)
            mp.put(analizer['jugadorLiberar'], liberar, listaJugadores)
        else:
            llaveValor=mp.get(analizer['jugadorLiberar'], liberar)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)
     else: 
        liberar=-1
        if mp.contains(analizer['jugadorLiberar'],liberar)==False:
            listaJugadores=lt.newList('ARRAY_LIST')
            lt.addLast(listaJugadores,liberar)
            mp.put(analizer['jugadorLiberar'], liberar, listaJugadores)
        else:
            llaveValor=mp.get(analizer['jugadorLiberar'], liberar)
            listaJugadores=me.getValue(llaveValor)
            lt.addLast(listaJugadores, jugador)

def jugadoresPorCaracteristica(analizer, segmentos, niveles, propiedad):
    if propiedad == 'overall':
        mapaPropiedad=analizer['jugadorOverall']
    if propiedad == 'potential':
        mapaPropiedad=analizer['jugadorPotencial']
    elif propiedad == 'value_eur':
        mapaPropiedad=analizer['jugadorValor']
    elif propiedad == 'wage_eur':
        mapaPropiedad=analizer['jugadorSalario']
    elif propiedad == 'age':
        mapaPropiedad=analizer['jugadorEdad']
    elif propiedad == 'height_cm':
        mapaPropiedad=analizer['jugadorAltura']
    elif propiedad == 'weight_cm':
        mapaPropiedad=analizer['jugadorPeso']
    elif propiedad == 'release_clause_eur':
        mapaPropiedad=analizer['jugadorValor']
    llaves=lt.newList('ARRAY_LIST')
    listaValoresFinal=lt.newList('ARRAY_LIST')
    listaAsteriscos=lt.newList('ARRAY_LIST')
    listaCount=lt.newList('ARRAY_LIST')
    menorLlave=om.minKey(mapaPropiedad)
    mayorLlave=om.maxKey(mapaPropiedad)
    intervaloGrande=mayorLlave-menorLlave
    intervalos=intervaloGrande/segmentos
    menorLlave=mayorLlave-intervalos
    i=1
    while i<=segmentos:
        listaValoresTodos=om.values(mapaPropiedad, menorLlave, mayorLlave)
        listaTemporal=lt.newList('ARRAY_LIST')
        for lista in lt.iterator(listaValoresTodos):
            for jugador in lt.iterator(lista):
                lt.addLast(listaTemporal,jugador)
        lt.addFirst(listaValoresFinal, (lt.size(listaTemporal)//niveles))
        lt.addFirst(listaAsteriscos, (lt.size(listaTemporal)//niveles)*'*')
        lt.addFirst(listaCount,lt.size(listaTemporal))
        tupla=(menorLlave, mayorLlave)
        lt.addFirst(llaves,tupla)
        menorLlave=menorLlave-intervalos
        mayorLlave=mayorLlave-intervalos
        i+=1
    print (listaCount)
    return llaves,listaCount, listaValoresFinal, listaAsteriscos
    







