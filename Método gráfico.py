# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:38:48 2020

@author:
    -Sebastian Salinas Rodriguez- 20181020058
    -Alex Humberto Rodriguez Rueda- 20181020088 
    -Ivan Santiago Chauta Gaviria- 20181020073
    
"""

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
'Ecuación: 2x+y<5'
eq5 = plot_implicit(2*x+y<5, (x,-10,10), (y,-10,10), line_color = 'b', show = True, 
                    title = '1) Región solución: 2x+y<5')
'--------------------------------------------------------------------------------------------------------------------'
#Punto 2
'Ecuación: y<=5'
eq4 = plot_implicit(y<=5, (x,-10,10), (y,-10,10), line_color = 'y', show = True,
                    title = '2) Región solución: y<=5')
'--------------------------------------------------------------------------------------------------------------------'
#Punto 3
'Ecuación: 2(2x-y)<2(x+y)-4'
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
'Ecuaciones: 2x+3y<=60'
'            x>=0'
'            y>=0'
solution = plot_implicit(And(2*x+3*y<=60,x>=0, y>=0 ) , (x,-5,40), (y,-5,40), line_color = 'b', show = True, 
                         title = '5) Región solución ecuaciones 1, 2 y 3')
'--------------------------------------------------------------------------------------------------------------------'

#Punto 6
'Función objetivo: 4x + 6y (maximizar)'
'Restricciones: 2x+y<=180'
'               x+2y<=160'
'               x+y<=100'


eq10 = plot_implicit(And(2*x+y<=180,x+2*y<=160,x+y<=100,x>=0,y>=0), (x,-5,100), (y,-5,100), line_color = 'y', show = True, 
                     title = '6) Región factible dadas las restricciones')

'--------------------------------------------------------------------------------------------------------------------'

#Primer ejercicio aplicación (maximizar)
'Restricciones:'
'5x+3y<=105'
'2x+4y<=70'
'x>=0'
'y>=0'

apl_1= plot_implicit(And(5*x+3*y <= 105, 2*x+4*y <=70, x>=0, y>=0), (x,-35,35), (y,-35,35),
                     line_color = 'b', show = True,title = 'Apl 1) Región factible para optimizar')

'P: 200x + 100y'

points = [(0,17),(15,10),(21,0)]
maximos = []

for i in points:
    maximos.append(200*i[0]+100*i[1])
    
print('Se deben producir '+str(max(maximos))+' productos para alcanzar una utilidad máxima')

'--------------------------------------------------------------------------------------------------------------------'

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

for i in points:
    minimos.append(500*i[0]+1100*i[1])
    
print('El costo mínimo de publicidad es '+str(min(minimos)))


#Tercer ejercicio aplicación (maximizar)

'Restricciones:'
'0.5x+0.8y<=10'
'0.75x+0.4y<=10'
'x<=y'
'x>=0'

apl_3= plot_implicit(And(0.5*x+0.8*y <=10, 0.75*x+0.4*y <=10, x<=y, x>=0), (x,-25,25), (y,-25,25),
                     line_color = 'g', show = True,title = 'Apl 3) Región factible para optimizar')

'P: 1000x + 1500y'

points = [(0,10),(0,12.5),(10,6.25),(11.33,3.77)]
maximos = []

for i in points:
    maximos.append(1000*i[0]+1500*i[1])
    
print('Los ingresos máximos equivalen a '+str(max(maximos)))

