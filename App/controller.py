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
 """

import config as cf
import model
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def inicializarAnalizer():
    return model.inicializarAnalizer()
    
def loadData(analizer, valor):
    tagsfile = cf.data_dir + 'FIFA/fifa-players-2022-utf8-'+valor+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for jugador in input_file:
        lista=model.addPlayerSofifaId(analizer, jugador)
        model.jugadoresClub(analizer, jugador)
        model.jugadoresPosicion(analizer, jugador)
        model.jugadorSalario(analizer, jugador)
        model.addPlayerBirthday(analizer, jugador)
        model.jugadorOverall(analizer, jugador)
        model.jugadorPotencial(analizer, jugador)
        model.jugadorValor(analizer, jugador)
        model.jugadorEdad(analizer, jugador)
        model.jugadorEstatura(analizer, jugador)
        model.jugadorPeso(analizer, jugador)
        model.jugadorLiberar(analizer, jugador)
    return lista
def jugadoresClubFecha(analizer, nombreClub):
    return model.jugadorClubFecha(analizer, nombreClub)

def jugadoresDesempenio(analizer, posicion, minOverall, maxOverall,minPotencial, maxPotencial, minSalario, maxSalario):
    return model.jugadoresDesempenio(analizer, posicion, minOverall, maxOverall,minPotencial, maxPotencial, minSalario, maxSalario)

def jugadoresSalarioCaracteristica(analizer,minSalario, maxSalario, caracteristica):
    return model.jugadoresSalarioCaracteristica(analizer,minSalario, maxSalario, caracteristica)

def jugadorFechaNacimiento(analizer, fechaInicio, fechaFinal, caracteristica):
    return model.jugadorFechaNacimiento(analizer, fechaInicio, fechaFinal, caracteristica)

def jugadoresPorCaracteristica(analizer, segmentos, niveles, propiedad):
    return model.jugadoresPorCaracteristica(analizer, segmentos, niveles, propiedad)