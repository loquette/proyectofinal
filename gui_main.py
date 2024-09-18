import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import webbrowser

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = entrada_usuario.get()
    if nombre_usuario:
        ventana_inicio.destroy()  # Cierra la ventana de inicio
        abrir_gestor_tareas(nombre_usuario)  # Abre la ventana del gestor de tareas
    else:
        messagebox.showerror("Error", "Por favor ingresa un nombre")

# Función para abrir la ventana del gestor de tareas
def abrir_gestor_tareas(nombre):
    global ventana_gestor
    ventana_gestor = tk.Tk()
    ventana_gestor.title(f"Gestor de Tareas - {nombre}")
    ventana_gestor.geometry("700x600")

    label_bienvenida = tk.Label(ventana_gestor, text=f"Bienvenido, {nombre}", font=("Arial", 16))
    label_bienvenida.pack(pady=10)

    boton_crear_tarea = tk.Button(ventana_gestor, text="Crear Tarea", command=abrir_crear_tarea)
    boton_crear_tarea.pack(pady=10)

    global lista_tareas
    lista_tareas = tk.Listbox(ventana_gestor, width=80, height=20)
    lista_tareas.pack(pady=10)

    ventana_gestor.mainloop()

# Ventana de inicio de sesión
ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("300x150")

label_usuario = tk.Label(ventana_inicio, text="Nombre de usuario:")
label_usuario.pack(pady=10)

entrada_usuario = tk.Entry(ventana_inicio)
entrada_usuario.pack(pady=5)

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack(pady=10)

ventana_inicio.mainloop()
