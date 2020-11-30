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
print(res)
print('La empresa pagaría, según esta asignación, ' + str(cost) + ' horas')