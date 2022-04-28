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
    print("0- Cargar información en el catálogo")
    print("1- las cinco adquisiciones más recientes de un club")
    print("2- los jugadores de cierta posición dentro de un rango de desempeño, potencial y salario")
    print('3- Reportar los jugadores dentro de un rango salarial y con cierta etiqueta: ')
    
def printResultsReq4(lista, sample, analizer):
    size=lt.size(lista)
    numJugadores=lt.size(lista)
    print("\nNumero de Jugadores que cumplen con los parámetros: " + str(numJugadores)+"\n")
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
            if jugador["player_tags"] == "":
                overall = "UNKNOWN"
            else: 
                overall= jugador["player_tags"]
            
            print("\nFecha de nacimiento: " + str(jugador["dob"]) + "\nDesempeño general: " + str(jugador["overall"]) + "\nPotencial: " + str(jugador["potential"])+ "\nNombre completo del jugador: " + str(jugador["long_name"])+ "\nEdad del jugador: " + str(jugador["age"]) 
            + "\nLiga a la que pertenece el club: " + str(jugador["league_name"]) + "\nClub actual: " + str(jugador["club_name"]) + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"])
            + "\nNacionalidad: " + str(jugador["nationality_name"]) + "\nValor del contrato del jugador: " + str(jugador["value_eur"]) + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) 
            + "\nComentarios: " + str(jugador["player_traits"]) + "\nEtiquetas: " + str(jugador["player_tags"]))
            i+=1
        print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("Los últimos 3 JUGADORES que cumplen los parámetros son: ")
        i = size-(sample-1)
        while i <= size:
            jugador= lt.getElement(lista, i)
            print("\nFecha de nacimiento: " + str(jugador["dob"]) + "\nDesempeño general: " + str(jugador["overall"]) + "\nPotencial: " + str(jugador["potential"])+ "\nNombre completo del jugador: " + str(jugador["long_name"])+ "\nEdad del jugador: " + str(jugador["age"]) 
            + "\nLiga a la que pertenece el club: " + str(jugador["league_name"]) + "\nClub actual: " + str(jugador["club_name"]) + "\nPosiciones en las que puede jugar: " + str(jugador["player_positions"])
            + "\nNacionalidad: " + str(jugador["nationality_name"]) + "\nValor del contrato del jugador: " + str(jugador["value_eur"]) + "\nValor del salario del jugador: " + str(jugador["wage_eur"]) 
            + "\nComentarios: " + str(jugador["player_traits"]) + "\nEtiquetas: " + str(jugador["player_tags"]))
            i+=1
        print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------')

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        analizer=controller.inicializarAnalizer()
        controller.loadData(analizer)

    elif int(inputs[0]) == 1: 
        nombreClub=input('Ingrese Nombre Club: ')
        listaJugadores=controller.jugadoresClubFecha(analizer, nombreClub)
        print(lt.size(listaJugadores))
        for jugador in lt.iterator(listaJugadores):
            print (jugador['short_name'])

    elif int(inputs[0]) == 2: 
        posicion=input('Ingrese la posicion deseada: ')
        minOverall=int(input('Minimo desempenio: '))
        maxOverall=int(input('Maximo desempenio: '))
        minPotencial=int(input('Minimo Potencial: '))
        maxPotencial=int(input('Maximo Potencial: '))
        minSalario=int(input('Minimo Salario: '))
        maxSalario=int(input('Maximo Salario: '))
        listaJugadores=controller.jugadoresDesempenio(analizer, posicion, minOverall, maxOverall, minPotencial, maxPotencial, minSalario, maxSalario)
        for jugador in lt.iterator(listaJugadores):
            print (jugador['short_name'])
            
    elif int(inputs[0])==3:
        minSalario=int(input('Límite inferior del salario recibido por los jugadores: '))
        maxSalario=int(input('Límite superior del salario recibido por los jugadores: ' ))
        caracteristica=(input('Una de las características que identifican a los jugadores '))
        listaJugadores=controller.jugadoresSalarioCaracteristica(analizer,minSalario, maxSalario, caracteristica)
        
        for jugador in lt.iterator(listaJugadores):
            print (jugador['short_name'])
    elif int(inputs[0])== 4:
        limiteInferiorFechaNacimiento=str(input("Límite inferior de la fecha de nacimiento del jugador: "))
        limiteSuperiorFechaNacimiento=str(input("Límite superior de la fecha de nacimiento del jugador: "))
        caracteristicaJugador=str(input("Una caracteristica que identifique al jugador: "))
        listaFinal= controller.jugadorFechaNacimiento(analizer, limiteInferiorFechaNacimiento, limiteSuperiorFechaNacimiento, caracteristicaJugador)
        printResultsReq4(listaFinal, 3, analizer)
    else:
        sys.exit(0)
