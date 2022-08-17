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
import controller
import config as cf
import sys
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo (cargar datos)")
    print("1- las cinco adquisiciones más recientes de un club (req 1) ")
    print("2- los jugadores de cierta posición dentro de un rango de desempeño, potencial y salario (req 2) ")
    print('3- Reportar los jugadores dentro de un rango salarial y con cierta etiqueta (req 3) ')
    print('4- Reportar los jugadores con cierto rasgo característico y nacidos en un periodo de tiempo (req 4) ')
    print('5- Graficar el histograma de una propiedad para los jugadores FIFA(req 5')
def printCargaDatos(lista, sample):
        size = lt.size(lista)
        numJugadoresTotal=lt.size(lista)
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print("El total de jugadores cargados desde el archivo son: " + str(numJugadoresTotal) + "\n")
    
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print("Los primeros cinco registros de JUGADORES cargados son: ")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        i = 1
        while i<=sample:
            jugador=lt.getElement(lista,i)
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else:
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["height_cm"] == "":
                altura = "UNKNOWN"
            else: 
                altura = jugador["height_cm"]
            if jugador["weight_kg"] == "":
                peso = "UNKNOWN"
            else: 
                peso = jugador["weight_kg"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["overall"] == "":
                overall= "UNKNOWN"
            else: 
                overall = jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["club_joined"] == "":
                fechaVinculacion = "UNKNOWN"
            else: 
                fechaVinculacion = jugador["club_joined"]
            if jugador["player_positions"] == "":
                jugadorPosiciones = "UNKNOWN"
            else: 
                jugadorPosiciones = jugador["player_positions"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_url"] == "":
                playerURL = "UNKNOWN"
            else: 
                playerURL = jugador["player_url"]
            print("\nNombre largo del jugador: " + str(longName) + "\nEdad: " + str(age) + "\nAltura(cm): " + str(altura) + "\nPeso(kg): " + str(peso) 
            + "\nNacionalidad: " + str(nacionalidad) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(valorSalario) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nLiga a la que pertenece: " + str(nombreLiga)
            + "\nClub a la que pertenece: " + str(nombreClub) + "\nFecha de vinculación al club: " + str(fechaVinculacion) + "\nPosiciones en las que juega: " + str(jugadorPosiciones) + "\nEtiquetas: " + str(playerTags)
            + "\nComentarios: " + str(playerTraits) + "\nURL perfil FIFA: " + str(playerURL))
            i+=1
        print("\n----------------------------------------------------------------------------------------------------------------------------------------")
        print("Los últimos cinco registros de JUGADORES son: ")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        i = size-(sample-1)
        while i <= size:
            jugador=lt.getElement(lista,i)
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else:
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["height_cm"] == "":
                altura = "UNKNOWN"
            else: 
                altura = jugador["height_cm"]
            if jugador["weight_kg"] == "":
                peso = "UNKNOWN"
            else: 
                peso = jugador["weight_kg"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["overall"] == "":
                overall= "UNKNOWN"
            else: 
                overall = jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["club_joined"] == "":
                fechaVinculacion = "UNKNOWN"
            else: 
                fechaVinculacion = jugador["club_joined"]
            if jugador["player_positions"] == "":
                jugadorPosiciones = "UNKNOWN"
            else: 
                jugadorPosiciones = jugador["player_positions"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_url"] == "":
                playerURL = "UNKNOWN"
            else: 
                playerURL = jugador["player_url"]
            print("\nNombre largo del jugador: " + str(longName) + "\nEdad: " + str(age) + "\nAltura(cm): " + str(altura) + "\nPeso(kg): " + str(peso) 
            + "\nNacionalidad: " + str(nacionalidad) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(valorSalario) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nLiga a la que pertenece: " + str(nombreLiga)
            + "\nClub a la que pertenece: " + str(nombreClub) + "\nFecha de vinculación al club: " + str(fechaVinculacion) + "\nPosiciones en las que juega: " + str(jugadorPosiciones) + "\nEtiquetas: " + str(playerTags)
            + "\nComentarios: " + str(playerTraits) + "\nURL perfil FIFA: " + str(playerURL))
            i+=1
        print("-------------------------------------------------------------------------------------------------------------------------------------")
def printResultsReq1(lista, sample):
    size =lt.size(lista)
    numJugadores=lt.size(lista)
    level=lt.getElement(lista,1)['league_level']
    leagueName=lt.getElement(lista,1)['league_name']
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nNumero total ADQUISICIONES del club: " + str(numJugadores))
    print('League Level: '+level)
    print('league Name: '+leagueName+'\n')
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    if size <= sample*1:
        print("Las adquisiciones organizadas por parámetros son: ")
        for jugador in lt.iterator(lista):
            if jugador["short_name"] == "":
                shortName= "UNKNOWN"
            else:
                shortName = jugador["short_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            if jugador["overall"] == "":
                overall= "UNKNOWN"
            else: 
                overall = jugador["overall"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["club_joined"] == "":
                fechaVinculacion = "UNKNOWN"
            else: 
                fechaVinculacion = jugador["club_joined"]
            if jugador["player_positions"] == "":
                jugadorPosiciones = "UNKNOWN"
            else: 
                jugadorPosiciones = jugador["player_positions"]
            if jugador["club_position"] == "":
                clubPosiciones = "UNKNOWN"
            else: 
                clubPosiciones = jugador["club_position"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nNombre corto del jugador: " + str(shortName) + "\nFecha de nacimiento: " + str(fechaNacimiento) + "\nEdad: " + str(age) 
            + "\nDesempeño general: " + str(overall) + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(valorSalario) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nFecha de vinculación al club: " + str(fechaVinculacion)
            + "\nPosiciones en las que puede jugar : " + str(jugadorPosiciones) + " y la que ocupa en el club: " + str(clubPosiciones) + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
    else:
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        print("Los cinco JUGADORES más recientemente vinculados al club son: ")
        i = 1
        while i<=sample:
            jugador = lt.getElement(lista, i)
            if jugador["short_name"] == "":
                shortName= "UNKNOWN"
            else:
                shortName = jugador["short_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            if jugador["overall"] == "":
                overall= "UNKNOWN"
            else: 
                overall = jugador["overall"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["club_joined"] == "":
                fechaVinculacion = "UNKNOWN"
            else: 
                fechaVinculacion = jugador["club_joined"]
            if jugador["player_positions"] == "":
                jugadorPosiciones = "UNKNOWN"
            else: 
                jugadorPosiciones = jugador["player_positions"]
            if jugador["club_position"] == "":
                clubPosiciones = "UNKNOWN"
            else: 
                clubPosiciones = jugador["club_position"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nNombre corto del jugador: " + str(shortName) + "\nFecha de nacimiento: " + str(fechaNacimiento) + "\nEdad: " + str(age) 
            + "\nDesempeño general: " + str(overall) + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(valorSalario) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nFecha de vinculación al club: " + str(fechaVinculacion)
            + "\nPosiciones en las que puede jugar : " + str(jugadorPosiciones) + " y la que ocupa en el club: " + str(clubPosiciones) + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
            i+=1
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------")

def printResultsReq2(lista, sample):
    size=lt.size(lista)
    nunJugadores = lt.size(lista)
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nNumero de JUGADORES que cumplen con los parámetros: " + str(nunJugadores) + "\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    if size <sample*2:
        print("Los jugadores organizados por parámetros son: ")
        for jugador in lt.iterator(lista):
            print("\nNombre corto del jugador: " + str(jugador["short_name"])+ "\nFecha de nacimiento y edad: " + str(jugador["dob"] + "y" + str(jugador["age"])) + "\nNacionalidad: " + str(jugador["nationality_name"]) + "\nValor del contrato del jugador: " + str(jugador["value_eur"])
            + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nValor de la cláusula de liberación del jugador: " + str(jugador["release_clause_eur"]) + "\nPotencial: " + str(jugador["potential"]) + "\nDesempeño general: " + str(jugador["overall"])
            + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"]) + "\nComentarios: " + str(jugador["player_traits"]) + "\nEtiquetas: " + str(jugador["player_tags"]))
    else:
        print("Los primeros 3 JUGADORES que cumplen los parámetros son: ")
        i = 1 
        while i <= sample:
            jugador=lt.getElement(lista, i)
            if jugador["short_name"] == "":
                shortName= "UNKNOWN"
            else: 
                shortName = jugador["short_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nNombre corto del jugador: " + str(shortName)+ "\nFecha de nacimiento y edad: " + str(fechaNacimiento)+ "y" + str(age) + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nPotencial: " + str(jugador["potential"]) + "\nDesempeño general: " + str(jugador["overall"])
            + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"]) + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
            i+=1
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Los ultimos 3 JUGADORES que cumplen con los parámetros son: ")
        i = size-(sample-1)
        while i <= size:
            jugador= lt.getElement(lista, i)
            if jugador["short_name"] == "":
                shortName= "UNKNOWN"
            else: 
                shortName = jugador["short_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["release_clause_eur"] == "":
                valorClausulaContrato = "UNKNOWN"
            else: 
                valorClausulaContrato = jugador["release_clause_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nNombre corto del jugador: " + str(shortName)+ "\nFecha de nacimiento y edad: " + str(fechaNacimiento) + " y " + str(age) + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nValor de la cláusula de liberación del jugador: " + str(valorClausulaContrato) + "\nPotencial: " + str(jugador["potential"]) + "\nDesempeño general: " + str(jugador["overall"])
            + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"]) + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
            i+=1
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------")

def printResultsReq3(lista, sample):
    size=lt.size(lista)
    numJugadores=lt.size(lista)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nNumero de Jugadores que cumplen con los parámetros: " + str(numJugadores) + "\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    if size <sample*2:
        print("Los jugadores organizados por parámetros son: ")
        for jugador in lt.iterator(lista):
            print("\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nDesempeño general: " + str(jugador["overall"]) + "\nPotencial: " + str(jugador["potential"]) + "\nNombre completo del jugador: " + str(jugador["long_name"]) + "\nFecha de nacimiento: " + str(jugador["dob"]) 
            + "\nEdad del jugador: " + str(jugador["age"]) + "\nLiga a la que pertenece el club: " + str(jugador["league_name"]) + "\nClub actual: " + str(jugador["club_name"]) + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"])
            + "\nNacionalidad: " + str(jugador["nationality_name"]) + "\nValor del contrato del jugador: " + str(jugador["value_eur"])
            + "\nComentarios: " + str(jugador["player_traits"]) + "\nEtiquetas: " + str(jugador["player_tags"]))
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------")

    else:
        print("Los primeros 3 JUGADORES que cumplen con los parámetros son: ")
        i=1
        while i<=sample:
            jugador=lt.getElement(lista, i)
            if jugador["overall"] == "":
                overall = "UNKNOWN"
            else: 
                overall= jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else: 
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["player_positions"] == "":
                posicion = "UNKNOWN"
            else: 
                posicion = jugador["player_positions"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            print("\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential) + "\nNombre completo del jugador: " + str(longName) + "\nFecha de nacimiento: " + str(fechaNacimiento) 
            + "\nEdad del jugador: " + str(age) + "\nLiga a la que pertenece el club: " + str(nombreLiga) + "\nClub actual: " + str(nombreClub) + "\nPosiciones en las que puede jugar: " + str(posicion)
            + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(jugador["player_tags"]))
            i += 1
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Los últimos 3 JUGADORES que cumplen los parámetros son: ")
        i = size-(sample-1)
        while i<=size:
            jugador=lt.getElement(lista,i)
            if jugador["overall"] == "":
                overall = "UNKNOWN"
            else: 
                overall= jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else: 
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["player_positions"] == "":
                posicion = "UNKNOWN"
            else: 
                posicion = jugador["player_positions"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["dob"] == "":
                fechaNacimiento = "UNKNOWN"
            else: 
                fechaNacimiento = jugador["dob"]
            print("\nValor del salario del jugador: " + str(jugador["wage_eur"]) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential) + "\nNombre completo del jugador: " + str(longName) + "\nFecha de nacimiento: " + str(fechaNacimiento) 
            + "\nEdad del jugador: " + str(age) + "\nLiga a la que pertenece el club: " + str(nombreLiga) + "\nClub actual: " + str(nombreClub) + "\nPosiciones en las que puede jugar: " + str(posicion)
            + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato)
            + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(jugador["player_tags"]))
            i+=1
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------")

def printResultsReq4(lista, sample):
    size=lt.size(lista)
    numJugadores=lt.size(lista)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nNumero de Jugadores que cumplen con los parámetros: " + str(numJugadores)+"\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    if size <= sample*2:
        print("Los jugadores organizados por parámetros son: ")
        for jugador in lt.iterator(lista):
            print("\nFecha de nacimiento: " + str(jugador["dob"]) + "\nDesempeño general: " + str(jugador["overall"]) + "\nPotencial: " + str(jugador["potential"])+ "\nNombre completo del jugador: " + str(jugador["long_name"])+ "\nEdad del jugador: " + str(jugador["age"]) 
            + "\nLiga a la que pertenece el club: " + str(jugador["league_name"]) + "\nClub actual: " + str(jugador["club_name"]) + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"])
            + "\nNacionalidad: " + str(jugador["nationality_name"]) + "\nValor del contrato del jugador: " + str(jugador["value_eur"]) + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) 
            + "\nComentarios: " + str(jugador["player_traits"]) + "\nEtiquetas: " + str(jugador["player_tags"]))
    else:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("Los primeros 3 JUGADORES que cumplen los parámetros son: ")
        i = 1
        while i <= sample:
            jugador= lt.getElement(lista, i)
            if jugador["overall"] == "":
                overall = "UNKNOWN"
            else: 
                overall= jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else: 
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["player_positions"] == "":
                posicion = "UNKNOWN"
            else: 
                posicion = jugador["player_positions"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nFecha de nacimiento: " + str(jugador["dob"]) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential)+ "\nNombre completo del jugador: " + str(longName)+ "\nEdad del jugador: " + str(age) 
            + "\nLiga a la que pertenece el club: " + str(nombreLiga) + "\nClub actual: " + str(nombreClub) + "\nPosiciones en las que puede jugar: " + str(posicion)
            + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato) + "\nValor del salario del jugador: " + str(valorSalario) 
            + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
            i+=1
        print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("Los últimos 3 JUGADORES que cumplen los parámetros son: ")
        i = size-(sample-1)
        while i <= size:
            jugador= lt.getElement(lista, i)
            if jugador["overall"] == "":
                overall = "UNKNOWN"
            else: 
                overall= jugador["overall"]
            if jugador["potential"] == "":
                potential = "UNKNOWN"
            else: 
                potential = jugador["potential"]
            if jugador["long_name"] == "":
                longName= "UNKNOWN"
            else: 
                longName = jugador["long_name"]
            if jugador["age"] == "":
                age = "UNKNOWN"
            else: 
                age = jugador["age"]
            if jugador["league_name"] == "":
                nombreLiga = "UNKNOWN"
            else: 
                nombreLiga = jugador["league_name"]
            if jugador["club_name"] == "":
                nombreClub = "UNKNOWN"
            else: 
                nombreClub = jugador["club_name"]
            if jugador["player_positions"] == "":
                posicion = "UNKNOWN"
            else: 
                posicion = jugador["player_positions"]
            if jugador["value_eur"] == "":
                valorContrato = "UNKNOWN"
            else: 
                valorContrato = jugador["value_eur"]
            if jugador["wage_eur"] == "":
                valorSalario = "UNKNOWN"
            else: 
                valorSalario = jugador["wage_eur"]
            if jugador["nationality_name"] == "":
                nacionalidad = "UNKNOWN"
            else: 
                nacionalidad = jugador["nationality_name"]
            if jugador["player_traits"] == "":
                playerTraits = "UNKNOWN"
            else: 
                playerTraits = jugador["player_traits"]
            if jugador["player_tags"] == "":
                playerTags = "UNKNOWN"
            else: 
                playerTags= jugador["player_tags"]
            print("\nFecha de nacimiento: " + str(jugador["dob"]) + "\nDesempeño general: " + str(overall) + "\nPotencial: " + str(potential)+ "\nNombre completo del jugador: " + str(longName)+ "\nEdad del jugador: " + str(age) 
            + "\nLiga a la que pertenece el club: " + str(nombreLiga) + "\nClub actual: " + str(nombreClub) + "\nPosiciones en las que puede jugar: " + str(posicion)
            + "\nNacionalidad: " + str(nacionalidad) + "\nValor del contrato del jugador: " + str(valorContrato) + "\nValor del salario del jugador: " + str(valorSalario) 
            + "\nComentarios: " + str(playerTraits) + "\nEtiquetas: " + str(playerTags))
            i+=1
        print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------')

def printReq5(llaves,listaCount, listaValoresFinal, listaAsteriscos, segmentos, niveles):
    i=1
    print('\n-------------------------------------------------------------------------------------------------------')
    while i<=segmentos:
        print('Bin '+str(i)+': '+str(lt.getElement(llaves, i))+' | '+'Count: ' +str(lt.getElement(listaCount,i))+' | '+
        'LVL: '+str(lt.getElement(listaValoresFinal,i)))
        i+=1
    i=1
    print('')
    while i<=segmentos:
        print('BIN'+' |'+lt.getElement(listaAsteriscos, i))
        i+=1
    print('\nCada "*" corresponde a '+str(niveles)+' jugadores\n')
    print('-------------------------------------------------------------------------------------------------------\n')

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        tamanioArchivo=input('Seleccione el tamanio del Alrchivo: \n1- Small \n2- Large\n')
        if tamanioArchivo=='2':
            tamanioArchivo='large'
        elif tamanioArchivo=='1':
            tamanioArchivo='small'
        print("Cargando información de los archivos ....")
        analizer=controller.inicializarAnalizer()
        listaData= controller.loadData(analizer, tamanioArchivo)
        listaData=om.valueSet(listaData)
        printCargaDatos(listaData,5)

    elif int(inputs[0]) == 1: 
        nombreClub=input('Ingrese Nombre Club: ')
        listaJugadores=controller.jugadoresClubFecha(analizer, nombreClub)
        printResultsReq1(listaJugadores, 5)

    elif int(inputs[0]) == 2: 
        posicion=input('Ingrese la posicion deseada: ')
        minOverall=int(input('Minimo desempenio: '))
        maxOverall=int(input('Maximo desempenio: '))
        minPotencial=int(input('Minimo Potencial: '))
        maxPotencial=int(input('Maximo Potencial: '))
        minSalario=int(input('Minimo Salario: '))
        maxSalario=int(input('Maximo Salario: '))
        listaJugadores=controller.jugadoresDesempenio(analizer, posicion, minOverall, maxOverall, minPotencial, maxPotencial, minSalario, maxSalario)
        printResultsReq2(listaJugadores, 3)
            
    elif int(inputs[0])==3:
        minSalario=int(input('Límite inferior del salario recibido por los jugadores: '))
        maxSalario=int(input('Límite superior del salario recibido por los jugadores: ' ))
        caracteristica=(input('Una de las características que identifican a los jugadores: '))
        listaJugadores=controller.jugadoresSalarioCaracteristica(analizer,minSalario, maxSalario, caracteristica)
        printResultsReq3(listaJugadores, 3)

    elif int(inputs[0])== 4:
        limiteInferiorFechaNacimiento=str(input("Límite inferior de la fecha de nacimiento del jugador: "))
        limiteSuperiorFechaNacimiento=str(input("Límite superior de la fecha de nacimiento del jugador: "))
        caracteristicaJugador=str(input("Una caracteristica que identifique al jugador: "))
        #Hola
        listaFinal= controller.jugadorFechaNacimiento(analizer, limiteInferiorFechaNacimiento, limiteSuperiorFechaNacimiento, caracteristicaJugador)
        printResultsReq4(listaFinal, 3)

    elif int(inputs[0])== 5:
        segmentos=int(input('Ingrese Numero de segmentos: '))
        niveles=int(input('Ingrese Numero niveles: '))
        propiedad=(input('Ingrese Propiedad: '))
        llaves,listaCount, listaValoresFinal, listaAsteriscos=controller.jugadoresPorCaracteristica(analizer, segmentos, niveles, propiedad)
        printReq5(llaves,listaCount, listaValoresFinal, listaAsteriscos, segmentos, niveles)
        

    else:
        sys.exit(0)
