from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import *
from tkinter import filedialog, Tk
import os

class ventana:
    def __init__(self, inter):
        self.interfaz = inter
        self.interfaz.geometry("1020x720")
        self.interfaz.title(" Bitxelart")
        self.crearVentana()

    def crearVentana(self):
        Button(self.interfaz, command=self.original, text="Original", font='arial 14', bg='white', fg='blue').place(
            x=50, y=120, width=130, height=30)
        Button(self.interfaz, command=self.original, text="Mirror X", font='arial 14', bg='white', fg='blue').place(
            x=50, y=230, width=130, height=30)
        Button(self.interfaz, command=self.original, text="Mirror Y", font='arial 14', bg='white', fg='blue').place(
            x=50, y=320, width=130, height=30)
        Button(self.interfaz, command=self.original, text="Double Mirror", font='arial 14', bg='white',
               fg='blue').place(x=50, y=420, width=130, height=30)

        barraMenu = Menu(self.interfaz)
        self.interfaz.config(menu=barraMenu, width=300, height=300)
        cargarMenu = Menu(barraMenu)
        analizarMenu = Menu(barraMenu)
        reportesMenu = Menu(barraMenu)
        salirMenu = Menu(barraMenu)

        barraMenu.add_cascade(label='Cargar', menu=cargarMenu)
        barraMenu.add_cascade(label='Analizar', menu=analizarMenu)
        barraMenu.add_cascade(label='Reportes', menu=reportesMenu)
        barraMenu.add_cascade(label='Salir', menu=salirMenu)

        cargarMenu.add_command(label='Seleccionar archivo', command = self.abrir)
        analizarMenu.add_command(label='Analizando')
        salirMenu.add_command(label='Salir del programa', command = self.salir)

    def original(self):
        print("Original")

    def abrir(self):
        Tk().withdraw()
        archivo = filedialog.askopenfile(
            title="Seleccionar un archivo LFP",
            initialdir="./",
            filetypes=(
                ("Archivos PXLA", "*.pxla"),
                ("Todos los archivos", "*.*")
            )
        )

        if archivo is None:
            print("Error de lectura")
            return None
        else:
            texto = archivo.read()
            archivo.close()
            print("Lectura Exitosa")
            return texto

    def salir(self):
        self.interfaz.destroy()

