from tkinter import*
from fileinput import filename
import os

from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
from tkinter import *
from tkinter import tix 
from tkinter.tix import Tree
from tkinter import ttk
import webbrowser
import tkinter as tk


def abrir_archivo():
        global filename
        x = ""
        #Tk().withdraw()
        try:       
            filename = askopenfilename(title="Selecciona un archivo",
                                       filetypes=[('Archivos',f'*.json'),
                                                  ('All Files', '*')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                
        except:
            print("Error, no se ha seleccionado ningun archivo")        
            return    
        texto = x
        cajaTexto1.delete(1.0,"end")
        cajaTexto1.insert(1.0, texto)     

def guarda_cambios():
        global filename
        resultado = cajaTexto1.get("1.0","end")   
        filenamen = open(filename, 'w')
        filenamen.write(resultado)
        filenamen.close()

def GuardarComo():
        global filename
        result= cajaTexto1.get("1.0","end")

        f = filedialog.asksaveasfile(mode='w')
    
        if f is None: # Devuelve ninguno si el dialogo se cerro con cancelar
            return
    
        f.write(result)
        f.close()
        
# Crear la ventana principal
principal = tk.Tk()
principal.title("Proyecto 2 LFP 1S2023")
principal.geometry("1000x550")
principal.configure(bg = "#102027")
BarraMenu = tk.Menu(principal)

MenuArchivo = tk.Menu(BarraMenu)
MenuAnalisis = tk.Menu(BarraMenu)
MenuTokens = tk.Menu(BarraMenu)
MenuErrores = tk.Menu(BarraMenu)

MenuArchivo.add_command(label="Nuevo")
MenuArchivo.add_command(label="Abrir", command=abrir_archivo)
MenuArchivo.add_command(label="Guardar", command=guarda_cambios)
MenuArchivo.add_command(label="Guardar Como", command=GuardarComo)
MenuArchivo.add_command(label="Salir", command= principal.destroy)

MenuAnalisis.add_command(label="Generar sentencias MongoDB")

MenuTokens.add_command(label="Ver tokens")

MenuErrores.add_command(label="Ver errores")

BarraMenu.add_cascade(label="Archivo", menu=MenuArchivo)
BarraMenu.add_cascade(label="Analisis", menu=MenuAnalisis)
BarraMenu.add_cascade(label="Tokens", menu=MenuTokens)
BarraMenu.add_cascade(label="Errores", menu=MenuErrores)

principal.config(menu=BarraMenu)


Frame = tk.Frame(height= 510, width=490)
Frame.config(bg='Blue')
Frame.place(x=10,y=30)
Frame2 = tk.Frame(height=510, width=490)
Frame2.config(bg='Green')
Frame2.place(x=500,y=30)  
Label1 = tk.Label(Frame, text="Entrada", font=('Times New Roman',13), fg='#000000', bg='White', width=20).place(x=150, y=10)
Label2 = tk.Label(Frame2, text="Salida", font=('Times New Roman',13), fg='#000000', bg='White', width=20).place(x=150, y=10)
cajaTexto1 = tk.Text(Frame, font=("Times New Roman",15),fg='black', width=45,height=20)
cajaTexto1.place(x=20,y=50)
cajaTexto2 = tk.Text(Frame2, font=("Times New Roman",15),fg='black', width=45,height=20)
cajaTexto2.place(x=20,y=50)



        
   



# Iniciar el bucle principal de la aplicación
principal.mainloop()

