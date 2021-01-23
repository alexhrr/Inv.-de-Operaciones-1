# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:43:11 2021

@author: sebas

"""
import pulp

# Ejercicio de aplicación utilizando PuLP
# Creamos la variable prob que contiene los datos del problema
prob = pulp.LpProblem("Problema de aplicación energía", pulp.LpMinimize)

# Creamos lista de plantas o nodos de oferta
plantas = ["Planta 1","Planta 2","Planta 3","Planta 4","Planta 5"]

# diccionario con la capacidad de oferta de cada planta
oferta = {"Planta 1": 80,
          "Planta 2": 30,
          "Planta 3": 60,
          "Planta 4": 65,
          "Planta 5": 75}

# Creamos la lista de las ciudades o nodos de demanda
ciudades = ["Cali", "Bogotá", "Medellín", "Cúcuta", "Barranquilla"]

# diccionario con la capacidad de demanda de cada ciudad
demanda = {"Cali":70,
           "Bogotá":40,
           "Medellín":70,
           "Cúcuta":35,
           "Barranquilla":95}

# Lista con los costos de transporte de cada nodo
costos = [   #ciudades
         #C B M U Q 
         [591,393,684,383,477],#1   Plantas
         [526,426,484,344,454],#2
         [481,516,656,292,553],#3
         [430,496,464,459,535],#4
         [390,535,628,329,517],#5
         ]

# Convertimos los costos en un diccionario de PuLP
costos = pulp.makeDict([plantas, ciudades], costos,0)

# Creamos una lista de tuplas que contiene todas las posibles rutas de tranporte.
rutas = [(c,b) for c in plantas for b in ciudades]

# creamos diccionario x que contendrá la candidad enviada en las rutas
x = pulp.LpVariable.dicts("ruta", (plantas, ciudades), 
                        lowBound = 0,
                        cat = pulp.LpInteger)

# Agregamos la función objetivo al problema
prob += sum([x[c][b]*costos[c][b] for (c,b) in rutas]), \
            "Suma_de_costos_de_transporte"

# Agregamos la restricción de máxima oferta de cada planta al problema.
for c in plantas:
    prob += sum([x[c][b] for b in ciudades]) <= oferta[c], \
            "Suma_de_Productos_que_salen_de_plantas_%s"%c

# Agregamos la restricción de demanda mínima de cada ciudad
for b in ciudades:
    prob += sum([x[c][b] for c in plantas]) >= demanda[b], \
    "Suma_de_productos_en_ciudades%s"%b
                   
# Los datos del problema son exportado a archivo .lp
prob.writeLP("problemaDeTransporte.lp")

# Resolviendo el problema.
prob.solve()

# Imprimimos el estado del problema.
print("Status: {}".format(pulp.LpStatus[prob.status]))
print()

print('# de Kw enviados desde las plantas:')
print()

# Imprimimos cada variable con su solución óptima.
for v in prob.variables():
    print("{0:} = {1:}".format(v.name, v.varValue))

print()

# Imprimimos el valor óptimo de la función objetivo   
print("Costo total de transporte = {}".format(prob.objective.value())) 