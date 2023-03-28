from fileinput import filename
import os
from tkinter import Tk, messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
from tkinter import *
from tkinter import tix 
from tkinter.tix import Tree
from tkinter import ttk
import webbrowser
from analizador_lexico import * #instruccion, operar_ , graficar 
import os


global cajaTexto

class Pantalla_Principal():
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Proyecto 1 LFP 1S2023")
        self.PP.geometry("1000x550")
        self.PP.configure(bg = "#102027")
        self.pantalla_1()
    
    def pantalla_1(self):
        self.Frame = Frame(height= 520, width=740)
        self.Frame.config(bg='Blue')
        self.Frame.place(x=10,y=20)
        self.Frame2 = Frame(height=520, width=240)
        self.Frame2.config(bg='Green')
        self.Frame2.place(x=750,y=20)  
        Label(self.Frame, text="Archivo", font=('Times New Roman',13), fg='#000000', bg='White', width=20).place(x=30, y=10)
        Label(self.Frame2, text="Ayuda", font=('Times New Roman',13), fg='#000000', bg='White', width=20).place(x=30, y=10)
        self.abrir = Button(self.Frame, text = "Abrir", command = self.abrir_archivo, background="Black", font=("Verdana",12), fg="white")
        self.abrir.place(x= 100,y=65)
        self.guardar = Button(self.Frame, text = "Guardar", command= self.guarda_cambios, background="Black", font=("Verdana",12), fg="white")
        self.guardar.place(x= 87,y=125)
        self.guardarComo = Button(self.Frame, text = "Guardar como", command= self.GuardarComo, background="Black", font=("Verdana",12), fg="white")
        self.guardarComo.place(x= 60,y=185)
        self.analizar = Button(self.Frame, text = "Analizar", command= self.ejecutar, background="Black", font=("Verdana",12), fg="white")
        self.analizar.place(x= 87,y=255)
        self.errores = Button(self.Frame, text = "Errores", command=self.getErrores, background="Black", font=("Verdana",12), fg="white")
        self.errores.place(x= 91,y=330)
        self.salir = Button(self.Frame, text = "Salir", command=self.PP.destroy, background="Red", font=("Verdana",12), fg="white")
        self.salir.place(x= 103,y=405)
        self.manual1 = Button(self.Frame2, text = "Manual de Usuario", command= self.abrir_manual1, background="Black", font=("Verdana",12), fg="white")
        self.manual1.place(x= 40,y=65)
        self.manual2 = Button(self.Frame2, text = "Manual Técnico", command= self.abrir_manual2, background="Black", font=("Verdana",12), fg="white")
        self.manual2.place(x= 54,y=125)
        self.ayuda = Button(self.Frame2, text = "Temas de Ayuda", command=self.Pantalla_Informacion, background="Black", font=("Verdana",12), fg="white")
        self.ayuda.place(x= 50,y=185)     
        self.cajaTexto = Text(self.Frame, font=("Times New Roman",15),fg='black', width=45,height=20)
        self.cajaTexto.place(x=237,y=40)
              
        self.Frame.mainloop()
      
    
    def Pantalla_Informacion(self):
        self.PP.withdraw()
        self.AA = Tk()
        self.AA.title("Temas de Ayuda")
        self.AA.geometry("500x250")
        self.AA.configure(bg = "#102027")
        self.frame = Frame (self.AA,height=210,width=480)
        self.frame.config(bg='Red')
        self.frame.place(x=10,y=20)
        Label(self.frame, text="Informacion del estudiante desarrollador", font=('Times New Roman',13), fg='#000000', bg='White', width=40).place(x=60, y=30)
        Label(self.frame, text="Nombre: David Eduardo Matias Ramirez", font=('Times New Roman',13), fg='#000000', bg='White', width=40).place(x=60, y=90)
        Label(self.frame, text="Carnet: 202006644", font=('Times New Roman',13), fg='#000000', bg='White', width=30).place(x=100, y=120)
        Label(self.frame, text="Cursando Lenguajes Formales y de Programacion", font=('Times New Roman',13), fg='#000000', bg='White', width=45).place(x=35, y=60)
        self.regresar = Button(self.frame, text = "Regresar", command= lambda: [f() for f in[self.PP.deiconify,self.AA.destroy]],  background="Black", font=("Verdana",9), fg="white")
        self.regresar.place(x= 205,y=160)     
        

    def abrir_archivo(self):
        global filename
        x = ""
        Tk().withdraw()
        try:       
            filename = askopenfilename(title="Selecciona un archivo",
                                       filetypes=[('Archivos',f'*.json'),
                                                  ('All Files', '*')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                
        except:
            print("Error, no se ha seleccionado ningun archivo")        
            return    
        self.texto = x
        self.cajaTexto.delete(1.0,"end")
        self.cajaTexto.insert(1.0, self.texto)        

    def guarda_cambios(self):
        global filename
        resultado = self.cajaTexto.get("1.0","end")   
        filenamen = open(filename, 'w')
        filenamen.write(resultado)
        filenamen.close()

    def GuardarComo(self):
        global filename
        result= self.cajaTexto.get("1.0","end")

        f = filedialog.asksaveasfile(mode='w')
    
        if f is None: # Devuelve ninguno si el dialogo se cerro con cancelar
            return
    
        f.write(result)
        f.close()
         

    def ejecutar(self):
        graficar()
        instruccion(self.cajaTexto.get(1.0, "end-1c"))
        respuestas = operar_()
        with open('Resultados_202006644.dot', 'w') as f:
            f.write(graficar())  
        os.system("dot -Tsvg Resultados_202006644.dot -o Resultados_202006644.svg")
        os.system('Resultados_202006644.svg')


        
    def abrir_manual1(self):
        webbrowser.open_new(r'C:\Users\david\OneDrive\Documentos\PROY1_LFPB+\Docs\Manual de Usuario Proyecto 1.pdf')

    def abrir_manual2(self):
        webbrowser.open_new(r'C:\Users\david\OneDrive\Documentos\PROY1_LFPB+\Docs\Manual Tecnico Proyecto 1.pdf')    

    def analizar(self):
        with open('Grafica.dot', 'w') as f:
            f.write(graficar())


    def getErrores(self):
        lista_errores = getErrores()
        contador = 1
        concatenando = " "
        concatenando += "{"
        while lista_errores:
            error = lista_errores.pop(0)
            concatenando += (error.operar(contador) + ",")

            contador += 1
        concatenando += "}"    
        h = open("Errores_202006644.json","w")    
        h.write(concatenando)
        

r = Pantalla_Principal()
