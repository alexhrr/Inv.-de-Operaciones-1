# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:18:38 2020

@author: FliaSalinasRodriguez
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:16:24 2020

@author: FliaSalinasRodriguez
"""

import pulp

# Ejemplo del problema de transporte de los buques utilizando PuLP
# Creamos la variable prob que contiene los datos del problema
prob = pulp.LpProblem("Problema de distribución de buques", pulp.LpMinimize)

# Creamos lista de puertos o nodos de oferta
puertos = ["Puerto 1", "Puerto 2", "Puerto 3"]

# diccionario con la capacidad de oferta de cada cerveceria
oferta = {"Puerto 1": 12,
          "Puerto 2": 14,
          "Puerto 3": 18}

# Creamos la lista de los bares o nodos de demanda
paises = ["País A", "País B", "País C", "País D"]

# diccionario con la capacidad de demanda de cada bar
demanda = {"País A":11,
           "País B":11,
           "País C":11,
           "País D":11,
           }

# Lista con los costos de transporte de cada nodo
costos = [   #Países
         #1 2 3 4
         [212,112,142,242],#A   Puertos
         [222,102,202,262],#B
         [222,142,102,222]#C
         ]

# Convertimos los costos en un diccionario de PuLP
costos = pulp.makeDict([puertos, paises], costos,0)

# Creamos una lista de tuplas que contiene todas las posibles rutas de tranporte.
rutas = [(c,b) for c in puertos for b in paises]

# creamos diccionario x que contendrá la candidad enviada en las rutas
x = pulp.LpVariable.dicts("ruta", (puertos, paises), 
                        lowBound = 0,
                        cat = pulp.LpInteger)

# Agregamos la función objetivo al problema
prob += sum([x[c][b]*costos[c][b] for (c,b) in rutas]), \
            "Suma_de_costos_de_transporte"

# Agregamos la restricción de máxima oferta de cada puerto al problema.
for c in puertos:
    prob += sum([x[c][b] for b in paises]) <= oferta[c], \
            "Suma_de_Productos_que_procesan_en_paises_%s"%c

# Agregamos la restricción de demanda mínima de cada pais
for b in paises:
    prob += sum([x[c][b] for c in puertos]) >= demanda[b], \
    "Sum_of_Products_into_Port%s"%b
                   
# Los datos del problema son exportado a archivo .lp
prob.writeLP("problemaDeTransporte.lp")

# Resolviendo el problema.
prob.solve()

# Imprimimos el estado del problema.
print("Status: {}".format(pulp.LpStatus[prob.status]))
print()

print('# de Cajas a enviar desde los puertos:')
print()

# Imprimimos cada variable con su solución óptima.
for v in prob.variables():
    print("{0:} = {1:}".format(v.name, v.varValue))

print()

# Imprimimos el valor óptimo de la función objetivo   
print("Costo total de transporte = {}".format(prob.objective.value()))