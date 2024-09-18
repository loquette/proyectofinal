import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import webbrowser
        return []

# Función para obtener la recomendación del clima
def get_weather_recommendation(pais, ciudad, fecha, hora):
    try:
        # Convertir la fecha y la hora a formato timestamp
        dt_str = f"{fecha} {hora}"
        dt = datetime.strptime(dt_str, "%m/%d/%y %H:%M")
        timestamp = int(dt.timestamp())
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
# Función para abrir el formulario de creación de tareas
def abrir_crear_tarea():
    ventana_tarea = tk.Toplevel()
    ventana_tarea.title("Crear Nueva Tarea")
    ventana_tarea.geometry("600x600")

    label_categoria = tk.Label(ventana_tarea, text="Selecciona la categoría:")
    label_categoria.pack(pady=5)

    # Categorías "Obra en campo" y "Reuniones"
    categorias = ["Obra en campo", "Reuniones"]
    categoria_seleccionada = tk.StringVar(value=categorias[0])

    menu_categorias = tk.OptionMenu(ventana_tarea, categoria_seleccionada, *categorias, command=lambda x: actualizar_formulario(categoria_seleccionada.get(), ventana_tarea))
    menu_categorias.pack(pady=5)

    # Elementos del formulario para "Obra en campo"
    label_ubicacion = tk.Label(ventana_tarea, text="Selecciona tu ubicación:")
    label_pais = tk.Label(ventana_tarea, text="País:")
    combo_pais = ttk.Combobox(ventana_tarea, values=paises, width=40)

    label_estado = tk.Label(ventana_tarea, text="Estado/Departamento:")
    combo_estado = ttk.Combobox(ventana_tarea, width=40)

    label_ciudad = tk.Label(ventana_tarea, text="Ciudad:")
    combo_ciudad = ttk.Combobox(ventana_tarea, width=40)

    label_fecha = tk.Label(ventana_tarea, text="Fecha:")
    entrada_fecha = DateEntry(ventana_tarea, width=12, background='darkblue', foreground='white', borderwidth=2)

    label_horario = tk.Label(ventana_tarea, text="Horario:")
    horario_frame = tk.Frame(ventana_tarea)
    horas = [f"{i:02d}" for i in range(24)]
    minutos = [f"{i:02d}" for i in range(60)]
    combo_horas = ttk.Combobox(horario_frame, values=horas, width=5)
    combo_horas.set("00")
    combo_minutos = ttk.Combobox(horario_frame, values=minutos, width=5)
    combo_minutos.set("00")

    label_especificaciones = tk.Label(ventana_tarea, text="Especificaciones del equipo:")
    entrada_especificaciones = tk.Entry(ventana_tarea, width=50)

    # Función para actualizar los departamentos basados en el país seleccionado
    def actualizar_estado(event):
        pais_seleccionado = combo_pais.get()
        departamentos = get_departamentos(pais_seleccionado)
        combo_estado['values'] = departamentos
        combo_estado.set('')

    # Función para actualizar las ciudades basadas en el departamento seleccionado
    def actualizar_ciudad(event):
        estado_seleccionado = combo_estado.get()
        ciudades = get_ciudades(estado_seleccionado)
        combo_ciudad['values'] = ciudades
        combo_ciudad.set('')
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
