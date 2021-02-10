# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:47:16 2021

@author: FliaSalinasRodriguez
"""

from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
#Se importa la librería del Algoritmo Húngaro
from hungarian_algorithm import algorithm

class Application(ttk.Frame):
    
    def calcular(self, mat):
            for k in mat:       
                print(k.get)
            
            lista = []    
            for s in mat:
                lista.append(s.get().split(","))
                
            print(lista)
                
            d = {}
            info = []
            for k in lista:
                for j in range(int(self.num_act.get())):
                    d[self.act_realizar[j]] = int(k[j])
                    info.append(d)
                d = {}
                    
            print("info")
            print(info)
            print(self.nom_empleado)
            
            g = dict(zip(self.nom_empleado, info))
            print(g)
            #Se asigna la tarea a cada empleado, cuyo costo es MENOR
            res = algorithm.find_matching(g, matching_type = 'min', return_type = 'list' )
            
            #Encontramos el costo mínimo
            cost =  algorithm.find_matching(g, matching_type = 'min', return_type = 'total' )
            
            #Imprimimos los resultados
            print(res)
            for i in res:
                for act in i:
                    if isinstance(act, tuple):
                        print("A "+str(act[0])+" le corresponde la actividad "+str(act[1])+".")
                        print()
                        messagebox.showinfo(message="A "+str(act[0])+" le corresponde la actividad "+str(act[1])+".", title="Asignación")
                    else:
                        print("En la que invierte "+str(act)+" minutos.")
                        print("Con un pago de $"+str(act*float(self.pago.get()))+'.')
                        print()
                        messagebox.showinfo(message="En la que invierte "+str(act)+" minutos. "+"Con un pago de $"+str(act*float(self.pago.get()))+'.', title="Costo Individual")
                        
                        print('La empresa pagaría, según esta asignación, ' + str(cost) + ' minutos.')
                        print('Con un gasto total de $'+str(cost*float(self.pago.get()))+'.')
                        print()
            messagebox.showinfo(message="La empresa pagaría, según esta asignación, " + str(cost) + " minutos.",title="Costo Empresarial")
                        
                                
    def obtener_datos(self):
        try:
            num_emp = int(self.num_emp.get())
            num_act = int(self.num_act.get())
            pago = float(self.pago.get())
            self.act_realizar = self.act_rel.get().split(",")
            self.nom_empleado = self.nom_emp.get().split(",")
        
            print(self.num_emp.get())
            print(self.num_act.get())
            print(self.pago.get())
            print(self.act_rel.get())
            print(self.nom_emp.get())
            print(self.act_realizar)
            print(self.nom_empleado)
            
            for c in range(0, num_emp + 1):
                for r in range(0, 2):
                    if(r==0 and c==0):
                        self.cell = ttk.Label(self, text="  ")
                        self.cell.grid(padx=5, pady=5, row=r, column=c)
                        self.cell.place(x=140+(30*r), y=140+(30*c))
                    else:
                        if(r==0 and c!=0):
                            self.cell = ttk.Label(self, text=self.nom_empleado[c-1])
                            self.cell.grid(padx=5, pady=5, row=r, column=c)
                            self.cell.place(x=140+(30*r), y=140+(30*c))
                        elif(r!=0 and c==0):
                            self.cell = ttk.Label(self, text="Tiempo actividades")
                            self.cell.grid(padx=5, pady=5, row=r, column=c)
                            self.cell.place(x=140+(30*r), y=140+(30*c))
                        else: 
                            self.mat = tk.StringVar()
                            self.cell = ttk.Entry(self, width=40, textvariable=self.mat)
                            self.cell.grid(padx=5, pady=5, row=r, column=c)
                            self.cell.place(x=240+(30*r), y=140+(30*c))
                            self.string_var_list.append(self.mat)
        except:
             messagebox.showerror(message="Error, la información ingresada no es válida", title="Error")
                                        
                                        
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Aplicación Modelo de asignación")
        
        self.num_emp = tk.StringVar()
        self.num_act = tk.StringVar()
        self.pago = tk.StringVar()
        self.act_rel = tk.StringVar()
        self.nom_emp = tk.StringVar()
        self.string_var_list = []
        
        main_window.configure(width=700, height=700)
        self.place(width=700, height=700)
      
        self.labelE = ttk.Label(self, text="Número de Empleados")
        self.labelE.place(x=10, y=10)
        
        self.n = ttk.Entry(self, textvariable=self.num_emp)
        self.n.place(x=160, y=10)
        
        self.labelA = ttk.Label(self, text="Número de Actividades")
        self.labelA.place(x=10, y=35)
        
        self.a = ttk.Entry(self, textvariable=self.num_act)
        self.a.place(x=160, y=35)
        
        self.labelP = ttk.Label(self, text="Pago por minuto")
        self.labelP.place(x=10, y=60)
        
        self.a = ttk.Entry(self, textvariable=self.pago)
        self.a.place(x=160, y=60)
        
        self.labelD = ttk.Label(self, text="Actividades realizadas")
        self.labelD.place(x=10, y=85)
        
        self.d = ttk.Entry(self, textvariable=self.act_rel, width=80)
        self.d.place(x=160, y=85)
        
        self.labelN = ttk.Label(self, text="Nombres Empleados")
        self.labelN.place(x=10, y=110)
        
        self.w = ttk.Entry(self, textvariable=self.nom_emp, width=80)
        self.w.place(x=160, y=110)

        self.entry = ttk.Button(self, text="Ingresar datos", command=self.obtener_datos)
        self.entry.place(x=10, y=135)
        
        self.calc = ttk.Button(self, text="Calcular asignación", command=lambda:self.calcular(self.string_var_list))
        self.calc.place(x=300, y=635)
   
     
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

