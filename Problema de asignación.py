# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:12:17 2020

@author: FliaSalinasRodriguez
"""

#Se importa la librería del Algoritmo Húngaro
from hungarian_algorithm import algorithm

#Creamos un grafo con los empleados, sus actividades y los costos respectivos
g = {
     'Empleado 1': {'C': 6, 'T': 8, 'A': 7},
     'Empleado 2': {'C': 7, 'T': 6, 'A': 8},
     'Empleado 3': {'C': 6, 'T': 8, 'A': 8}
     }

#Se asigna la tarea a cada empleado, cuyo costo es MENOR
res = algorithm.find_matching(g, matching_type = 'min', return_type = 'list' )

#Encontramos el costo mínimo
cost =  algorithm.find_matching(g, matching_type = 'min', return_type = 'total' )

#Imprimimos los resultados
print()
print(res)
print('La empresa pagaría, según esta asignación, ' + str(cost) + ' horas')
print()

'Ejemplo 2'

#Creamos un grafo con los empleados, sus actividades y los costos respectivos
g = {
     'Empleado 1': {'C': 1, 'T': 4,'D': 6, 'A': 3},
     'Empleado 2': {'C': 9, 'T': 7,'D': 10, 'A': 9},
     'Empleado 3': {'C': 4, 'T': 5,'D': 11, 'A': 7},
     'Empleado 4': {'C': 8, 'T': 7,'D': 8, 'A': 5}
     }

#Se asigna la tarea a cada empleado, cuyo costo es MENOR
res = algorithm.find_matching(g, matching_type = 'min', return_type = 'list' )

#Encontramos el costo mínimo
cost =  algorithm.find_matching(g, matching_type = 'min', return_type = 'total' )

#Imprimimos los resultados
print(res)
print('La empresa pagaría, según esta asignación, ' + str(cost) + ' horas')