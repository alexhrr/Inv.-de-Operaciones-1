# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:38:48 2020

@author:
    -Sebastian Salinas Rodriguez- 20181020058
    -Alex Humberto Rodriguez Rueda- 20181020088 
    -Ivan Santiago Chauta Gaviria- 20181020073
    
"""


#Importación de librerias y declaración de símbolos

from __future__ import division
from sympy import *
from IPython.display import Markdown as md
from IPython.display import display
from sympy import solve_poly_inequality, reduce_abs_inequality
from sympy.solvers.inequalities import solve_univariate_inequality, reduce_rational_inequalities
from sympy.parsing.latex import parse_latex

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing(use_latex=False)
X1,X2=symbols('X1 X2')

'--------------------------------------------------------------------------------------------------------------------'
#Punto 1
'Región solución inecuación: 2x+y<5'
eq5 = plot_implicit(2*x+y<5, (x,-10,10), (y,-10,10), line_color = 'b', show = True, 
                    title = '1) Región solución: 2x+y<5')
'--------------------------------------------------------------------------------------------------------------------'
#Punto 2
'Región solución inecuación: y<=5'
eq4 = plot_implicit(y<=5, (x,-10,10), (y,-10,10), line_color = 'y', show = True,
                    title = '2) Región solución: y<=5')
'--------------------------------------------------------------------------------------------------------------------'
#Punto 3
'Región solución inecuación: 2(2x-y)<2(x+y)-4'
eq9 = plot_implicit(2*(2*x-y)<2*(x+y)-4, (x,-30,30), (y,-30,30), line_color = 'r', show = True, 
                    title = '3) Región solución: 2(2x-y)<2(x+y)-4')

'--------------------------------------------------------------------------------------------------------------------'
#Punto 4
'Ecuaciones: 2x+y>3'
'            2y-1>0'
'            x>=y'
solution = plot_implicit(And(2*x+y>3, 2*y-1>0, x>=y) , (x,-5,5), (y,-5,5), line_color = 'g', show = True, 
                         title = '4) Región solución ecuaciones 1, 2 y 3')

'--------------------------------------------------------------------------------------------------------------------'
#Punto 5
'Región solución inecuaciones: 2x+3y<=60'
'            x>=0'
'            y>=0'
solution = plot_implicit(And(2*x+3*y<=60,x>=0, y>=0 ) , (x,-5,40), (y,-5,40), line_color = 'b', show = True, 
                         title = '5) Región solución ecuaciones 1, 2 y 3')
'--------------------------------------------------------------------------------------------------------------------'

#Punto 6
'Maximización:'
'P: 4x + 6y'
'Restricciones: 2x+y<=180'
'               x+2y<=160'
'               x+y<=100'


eq10 = plot_implicit(And(2*x+y<=180,x+2*y<=160,x+y<=100,x>=0,y>=0), (x,-5,100), (y,-5,100), line_color = 'y', show = True, 
                     title = '6) Región factible dadas las restricciones')

'--------------------------------------------------------------------------------------------------------------------'
'''
Ejercicio de aplicación 1: Una compañía fabrica 2 productos X y Y, cada uno requiere cierto tiempo en la línea de 
ensamblado y de acabado. Cada artículo X necesita 5 horas de ensamblado y 2 de acabado, y cada artículo de tipo Y
 necesita 3 horas de ensamblado y 4 de acabado. La empresa se dispone de la siguiente manera:

*   105 horas en el ensamblaje
*   70 horas en el acabado

La empresa puede vender todos los artículos y obtener una utilidad de:


*   200 por cada X
*   100 por cada Y

Determinar el número de artículos de cada tipo que se deben fabricar, para maximizar la utilidad:
'''
#Primer ejercicio aplicación (maximizar)
'Restricciones:'
'5x+3y<=105'
'2x+4y<=70'
'x>=0'
'y>=0'
'P: 200x + 100y'

apl_1= plot_implicit(And(5*x+3*y <= 105, 2*x+4*y <=70, x>=0, y>=0), (x,-35,35), (y,-35,35),
                     line_color = 'b', show = True,title = 'Apl 1) Región factible para optimizar')


points = [(0,17),(15,10),(21,0)]
maximos = []

print("De acuerdo al método gráfico, los posibles puntos solución son:")
for i in points:
    print("x="+str(i[0])+", y="+str(i[1]))

for i in points:
    maximos.append(200*i[0]+100*i[1])
    
    
print('Se deben producir '+str(max(maximos))+' productos para alcanzar una utilidad máxima')

for i in points:
    if(200*i[0]+100*i[1] == max(maximos)):
        print('En el punto: x='+str(i[0])+' y='+str(i[1]))

'--------------------------------------------------------------------------------------------------------------------'
'''
Ejercicio de aplicación 2: Una empresa de publicidad tiene en consideración dos métodos de difusión para su comercial,
denominados X y Y:

*   X llega al 2% de las familias de ingresos altos y al 3% de ingresos medios
*   Y llega al 3% de las familias de ingresos altos y al 6% de ingresos medios

El costo de publicidad por el medio X vale 500 y por el lado de Y vale 1100. El objetivo es llegar como mínimo al 36% 
de altos ingresos y al 60% de ingresos medios, minimizando el costo de publicidad.
'''
# Segundo ejercicio aplicación (minimizar)

'Restricciones:'
'2x+3y<=36'
'3x+6y<=60'
'x>=0'
'y>=0'

apl_2= plot_implicit(And(2*x+3*y <= 36, 3*x+6*y <=60, x>=0, y>=0), (x,-25,25), (y,-25,25),
                     line_color = 'r', show = True,title = 'Apl 2) Región factible para optimizar')

'P: 500x + 1100y'

points = [(0,10),(12,4),(18,0)]
minimos = []

print("De acuerdo al método gráfico, los posibles puntos solución son:")
for i in points:
    print("x="+str(i[0])+", y="+str(i[1]))

for i in points:
    minimos.append(500*i[0]+1100*i[1])
    
print('El costo mínimo de publicidad es '+str(min(minimos)))

for i in points:
    if(500*i[0]+1100*i[1] == max(minimos)):
        print('En el punto: x='+str(i[0])+' y='+str(i[1]))

'--------------------------------------------------------------------------------------------------------------------'
#Tercer ejercicio aplicación (maximizar)
'''
Ejercicio de aplicación 3: Una fábrica de fertilizantes produce dos tipos de abono A y B, a partir de dos materias 
primas M1 y M2. Para fabricar una tonelada de A, hacen 500kg de M1 y 750kg de M2; y para B son 800kg de M1 y 400kg 
de M2. La empresa tiene contratado un suministro máximo de 10 Toneladas de materia prima y vende a 1000 y 1500 euros 
por tonelada de A y B respectivamente.

Sabiendo que la demanda de B nunca puede triplicar la demanda de A, Cuántas toneladas de abono debe fabricar para 
maximizar sus ingresos y cuales son?

'''
'Restricciones:'
'0.5x+0.8y<=10'
'0.75x+0.4y<=10'
'x<=y'
'x>=0'
'P: 1000x + 1500y'

apl_3= plot_implicit(And(0.5*x+0.8*y <=10, 0.75*x+0.4*y <=10, x<=y, x>=0), (x,-25,25), (y,-25,25),
                     line_color = 'g', show = True,title = 'Apl 3) Región factible para optimizar')

points = [(0,10),(0,12.5),(10,6.25),(11.33,3.77)]
maximos = []
print("De acuerdo al método gráfico, los posibles puntos solución son:")
for i in points:
    print("x="+str(i[0])+",y="+str(i[1]))

for i in points:
    maximos.append(1000*i[0]+1500*i[1])
    
print('Los ingresos máximos equivalen a '+str(max(maximos)))

for i in points:
    if(1000*i[0]+1500*i[1] == max(maximos)):
        print('En el punto: x='+str(i[0])+' y='+str(i[1]))

'--------------------------------------------------------------------------------------------------------------------'