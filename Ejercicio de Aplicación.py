# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:25:31 2021

@author: FliaSalinasRodriguez
"""

#Se importa la librería del Algoritmo Húngaro
from hungarian_algorithm import algorithm

n = int(input("cantidad de empleados:"))   
a = int(input("cantidad de actividades:"))    
p = float(input("pago por minuto:"))     
d ={} 
lab = input("Actividades a desarrollar").split()

names = []
info = []    


#Ciclo for para obtener los datos necesarios                
for i in range(n):   
    name = str(input("Nombre del empleado: "))
    for j in range(a):    
        text = input("Horas empleadas por actividad: ")
        d[lab[j]] = int(text)
    names.append(name) 
    info.append(d)
    d ={} 

g = dict(zip(names, info))

#Se asigna la tarea a cada empleado, cuyo costo es MENOR
res = algorithm.find_matching(g, matching_type = 'min', return_type = 'list' )

#Encontramos el costo mínimo
cost =  algorithm.find_matching(g, matching_type = 'min', return_type = 'total' )

#Imprimimos los resultados
print()
for i in res:
    for act in i:
        if isinstance(act, tuple):
            print("A "+str(act[0])+" le corresponde la actividad "+str(act[1])+".")
            print()
        else:
            print("En la que invierte "+str(act)+" minutos.")
            print("Con un pago de $"+str(act*p)+'.')
            print()
        
print('La empresa pagaría, según esta asignación, ' + str(cost) + ' minutos.')
print('Con un gasto total de $'+str(cost*p)+'.')
print()
