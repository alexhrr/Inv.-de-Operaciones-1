# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:07:22 2021

@author: FliaSalinasRodriguez
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy import stats
from tkinter import messagebox
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import chisquare
from scipy.stats import chi2

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        self.ventana1.configure(width=400, height=400)
        self.ventana1.title("Programa Estadistica")
        opciones1 = tk.Menu(menubar1)
        
        opciones1.add_command(label="Medidas Estadisticas", command = lambda:self.med_est(self.ventana1))
        opciones1.add_command(label="Teorema de Bayes", command = lambda:self.teor_bayes(self.ventana1))
        opciones1.add_command(label="Prueba Chi2", command = lambda:self.test_chi(self.ventana1))
        menubar1.add_cascade(label="Opciones", menu=opciones1)  
        
        opciones2= tk.Menu(menubar1)
        opciones2.add_command(label="Verificar", command = lambda:self.mejor_aj(self.ventana1))
        menubar1.add_cascade(label="Ajuste Optimo", menu=opciones2) 
        
        opciones3 = tk.Menu(menubar1)
        opciones3.add_command(label="Limpiar", command=self.limpiar_ventana)
        opciones3.add_command(label="Salir", command=self.cerrar_ventana)
        menubar1.add_cascade(label="Ventana", menu=opciones3) 
        
        
        self.ventana1.mainloop()
        

    def med_est(self, ventana1):
        
        self.ventana1.geometry("500x200")

        self.etiqueta = ttk.Label(ventana1, text="Cantidad de datos:")
        self.etiqueta.place(x=20, y=20)

        self.texto = ttk.Entry(ventana1)
        self.texto.place(x=160, y=20)

        self.etiqueta2 = ttk.Label(ventana1, text="Datos:")
        self.etiqueta2.place(x=20, y=60)

        self.texto2 = ttk.Entry(ventana1)
        self.texto2.place(x=160, y=60)
        
        self.boton = ttk.Button(ventana1, text="Calcular desviacion tipica", command=self.calc_med_est)
        self.boton.place(x=200, y=110)
        
    def teor_bayes(self, ventana1):
        
        ventana1.geometry("500x200")

        self.etiqueta = ttk.Label(ventana1, text="Tasa Base:")
        self.etiqueta.place(x=20, y=20)

        self.texto = ttk.Entry(ventana1)
        self.texto.place(x=160, y=20)

        self.etiqueta2 = ttk.Label(ventana1, text="Sensibilidad:")
        self.etiqueta2.place(x=20, y=60)

        self.texto2 = ttk.Entry(ventana1)
        self.texto2.place(x=160, y=60)

        self.etiqueta3 = ttk.Label(ventana1, text="Especificidad:")
        self.etiqueta3.place(x=20, y=100)

        self.texto3 = ttk.Entry(ventana1)
        self.texto3.place(x=160, y=100)
        
        self.boton = ttk.Button(ventana1, text="Calcular ", command= lambda : self.bayes_theorem(eval(self.texto.get()), eval(self.texto2.get()), eval(self.texto3.get())))
        self.boton.place(x=200, y=150)
       
        
    def test_chi(self,ventana1):
        
        ventana1.configure(width=950, height=400)
        
        datosA = tk.StringVar()
        
        left_frame = tk.Frame(ventana1)
        left_frame.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.9)

        right_frame = tk.Frame(ventana1, bg='#C0C0C0', bd=1.5)
        right_frame.place(relx=0.3, rely=0.05, relwidth=0.65, relheight=0.9)
        
        ventana1.labelA = ttk.Label(left_frame, text="Conjunto A:")
        ventana1.labelA.place(x=10, y=10)
        
        ventana1.n1 = ttk.Entry(left_frame, textvariable=datosA)
        ventana1.n1.place(x=100, y=10)
        
        ventana1.btn = ttk.Button(left_frame, text="Prueba Chi2", command = lambda: self.chi2_proof(datosA))
        ventana1.btn.place(x=10, y=35)
        
        #--- Agregar figura ---
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax = figure.add_subplot(111)
        self.ax.grid(True),self.ax.set_xlabel('x'),self.ax.set_ylabel('y')
        self.ax.set_title('Distribucion Chi2')
        self.line = FigureCanvasTkAgg(figure, right_frame)   
        self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        #----------------------
    
    def mejor_aj(self, ventana1):
        ventana1.configure(width=300, height=300)
        
        datosA = tk.StringVar()
        datosB = tk.StringVar()
        
        
        ventana1.labelA = ttk.Label(ventana1, text="Conjunto A:")
        ventana1.labelA.place(x=10, y=10)
        
        ventana1.n1 = ttk.Entry(ventana1, textvariable=datosA)
        ventana1.n1.place(x=100, y=10)
        
        ventana1.labelB = ttk.Label(ventana1, text="Conjunto B:")
        ventana1.labelB.place(x=10, y=35)
        
        ventana1.n2 = ttk.Entry(ventana1, textvariable=datosB)
        ventana1.n2.place(x=100, y=35)
        
        ventana1.btn = ttk.Button(ventana1, text="Mejor Ajuste", command = lambda: self.definir_mejor_ajuste(datosA,datosB))
        ventana1.btn.place(x=10, y=60)
        
        
    def calc_med_est(self):
        d=self.texto.get()
        datos = self.texto2.get()
        datos2= eval(datos)
        datos3 = np.array(datos2)

        if eval(d) == len(datos3):
            prom = np.std(datos3)
            mean = np.mean(datos3)
            median = np.median(datos3)
            var = np.var(datos3)
            
            messagebox.showinfo(message="La desviacion tipica es: " + str(round(prom,3))+"\n"+
                                "La media es: " + str(round(mean,3))+"\n"+
                                "La mediana es: " + str(round(median,3))+"\n"+
                                "La varianza es: " + str(round(var,3))+".")
        else:
            messagebox.showinfo(message="La cantidad de datos ingresados no es correcta")
        
        
    def bayes_theorem(self, p_a, p_b_given_a, p_not_b_given_not_a):
        # calcular P (no A)
        not_a = 1 - p_a
        # calcular P (B | no A)
        b_given_not_a = 1 - p_not_b_given_not_a
        # calcular P (A | B)
        p_a_given_b = (p_b_given_a * p_a) / (p_b_given_a * p_a + b_given_not_a * not_a)

        messagebox.showinfo(message='P (A | B) =% .3f %%' % (p_a_given_b * 100), title="Resultado")
        

    def chi2_proof(self, p):
        a = p.get().split(",")
        print(a)
 
        a = np.array(a).astype(np.float)
        
        print(a)
        
        c2, p = chisquare(a)
        
        print("c2 = " + str(c2))
        print("p = " + str(p))      
        messagebox.showinfo(message= "La c2-estadistica para estos datos es: "+str(c2)+".\n"+
                            "El valor p para estos datos es: "+str(p)+".", title="resultado")
        
        N = a.size
        df = N - 1
        
        a = np.sort(a)
                
        self.ax.plot
        self.ax.clear()
        self.ax.plot(a, chi2.pdf(a, df), 'r-', lw=5, alpha=0.6, label='chi2 pdf'), self.ax.grid(True)
        self.ax.legend(['Conjunto a'])
        self.ax.set_xlabel('x'),self.ax.set_ylabel('y')
        self.ax.set_title('Distribucion Chi2')
        self.line.draw()
        
        
    def definir_mejor_ajuste(self, p ,q):
        
        a = p.get().split(",")
        b = q.get().split(",")
        
        print(a)
        print(b)
        
        a = np.array(a).astype(np.float)
        b = np.array(b).astype(np.float)
        
        print(a)
        print(b)
        
        
        #T-Student
        N = a.size
        
        var_a = a.var(ddof=1)
        var_b = b.var(ddof=1)
        
        s = np.sqrt((var_a + var_b)/2)
        
        te = (a.mean() - b.mean())/(s*np.sqrt(2/N))
        
        df = N - 1 
        #p-value after comparison with the t 
        p_tst = 1 - stats.t.cdf(te,df=df)
        
        #Chi2
        
        c2_A, p_chi2_A = chisquare(a)
        
        c2_B, p_chi2_B = chisquare(a)
        
        if(p_tst > 0.9):
            messagebox.showinfo(message= "El mejor ajuste para estos datos es t-student.\n"+
                            "El valor p para estos datos es: "+str(p_tst)+".", title="resultado")
        elif(p_tst <= 0.9 and p_chi2_A > 0.9):
            messagebox.showinfo(message= "El mejor ajuste para el conjunto A es chi2.\n"+
                            "El valor p para estos datos es: "+str(p_chi2_A)+".", title="resultado")       
        elif(p_tst <= 0.9 and p_chi2_B > 0.9):
            messagebox.showinfo(message= "El mejor ajuste para el conjunto B es chi2.\n"+
                            "El valor p para estos datos es: "+str(p_chi2_B)+".", title="resultado")
        else:
            messagebox.showinfo(message= "Quizá debería utilizarse Bayes para estos datos.\n"+
                            "Los valores p para estos datos es: "+str(p_chi2_A)+", "+str(p_chi2_B)+", "+str(p_tst)+".", title="resultado")
            
            
        
    def cerrar_ventana(self):
        self.ventana1.destroy()
        
    def limpiar_ventana(self):
        self.ventana1.destroy()
        aplicacion1=Aplicacion()


aplicacion1=Aplicacion()

