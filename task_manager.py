# Función para mostrar u ocultar campos según la categoría seleccionada
    def actualizar_formulario(categoria, ventana):
        if categoria == "Obra en campo":
            # Mostrar campos para "Obra en campo"
            label_ubicacion.pack(pady=5)
            label_pais.pack(pady=5)
            combo_pais.pack(pady=5)
            combo_pais.bind("<<ComboboxSelected>>", actualizar_estado)

            label_estado.pack(pady=5)
            combo_estado.pack(pady=5)
            combo_estado.bind("<<ComboboxSelected>>", actualizar_ciudad)

            label_ciudad.pack(pady=5)
            combo_ciudad.pack(pady=5)

            label_fecha.pack(pady=5)
            entrada_fecha.pack(pady=5)
            label_horario.pack(pady=5)
            horario_frame.pack(pady=5)
            combo_horas.pack(side=tk.LEFT, padx=5)
            combo_minutos.pack(side=tk.LEFT, padx=5)
            label_especificaciones.pack(pady=5)
            entrada_especificaciones.pack(pady=5)

            # Botón para obtener la recomendación del clima
            def obtener_recomendacion_clima():
                pais = combo_pais.get()
                ciudad = combo_ciudad.get()
                fecha = entrada_fecha.get_date().strftime("%m/%d/%y")
                hora = f"{combo_horas.get()}:{combo_minutos.get()}"
                clima = get_weather_recommendation(pais, ciudad, fecha, hora)
                mensaje_clima.config(text=f"Recomendación del clima: {clima}")

            boton_obtener_clima = tk.Button(ventana_tarea, text="Obtener Recomendación del Clima", command=obtener_recomendacion_clima)
            boton_obtener_clima.pack(pady=10)

            # Mensaje de recomendación del clima
            mensaje_clima = tk.Label(ventana_tarea, text="")
            mensaje_clima.pack(pady=5)

            # Botón para crear y almacenar la tarea
            def crear_tarea():
                pais = combo_pais.get()
                estado = combo_estado.get()
                ciudad = combo_ciudad.get()
                fecha = entrada_fecha.get_date().strftime("%m/%d/%y")
                hora = f"{combo_horas.get()}:{combo_minutos.get()}"
                especificaciones = entrada_especificaciones.get()
                clima = get_weather_recommendation(pais, ciudad, fecha, hora)
                tarea = f"Obra en campo: {ciudad}, {estado}, {pais} - Fecha: {fecha}, Hora: {hora} - Especificaciones: {especificaciones} - {clima}"
                lista_tareas.insert(tk.END, tarea)
                ventana_tarea.destroy()

            boton_crear_tarea = tk.Button(ventana_tarea, text="Crear Tarea", command=crear_tarea)
            boton_crear_tarea.pack(pady=10)
            
        elif categoria == "Reuniones":
            # Mostrar campos para "Reuniones"
            label_fecha.pack(pady=5)
            entrada_fecha.pack(pady=5)
            label_horario.pack(pady=5)
            horario_frame.pack(pady=5)
            combo_horas.pack(side=tk.LEFT, padx=5)
            combo_minutos.pack(side=tk.LEFT, padx=5)

            # Campo para enlace de Google Meet
            label_enlace = tk.Label(ventana_tarea, text="Enlace de Google Meet:")
            entrada_enlace = tk.Entry(ventana_tarea, width=50)
            label_enlace.pack(pady=5)
            entrada_enlace.pack(pady=5)
          
            # Botón para acceder al enlace de Google Meet
            def acceder_meet():
                enlace = entrada_enlace.get()
                if enlace and enlace.startswith(('http://', 'https://')):
                    webbrowser.open(enlace)
                else:
                    messagebox.showerror("Error", "Por favor ingresa un enlace válido que comience con http:// o https://")

            boton_acceder_meet = tk.Button(ventana_tarea, text="Acceder a Google Meet", command=acceder_meet)
            boton_acceder_meet.pack(pady=10)

            # Mostrar solo calendario y generar enlace para Google Meet
            label_fecha.pack(pady=5)
            entrada_fecha.pack(pady=5)

            def abrir_google_meet():
                # Abre la página principal de Google Meet
                url_meet = "https://meet.google.com/"
                webbrowser.open(url_meet)  # Abrir automáticamente la página de Google Meet
                messagebox.showinfo("Reunión", "Se ha abierto la página de Google Meet.")

            boton_enlace = tk.Button(ventana, text="Abrir Google Meet", command=abrir_google_meet)
            boton_enlace.pack(pady=10)

            # Botón para crear y almacenar la tarea
            def crear_tarea_reunion():
                fecha = entrada_fecha.get_date().strftime("%m/%d/%y")
                hora = f"{combo_horas.get()}:{combo_minutos.get()}"
                enlace = entrada_enlace.get()
                tarea = f"Reunión - Fecha: {fecha}, Hora: {hora} - Enlace de Meet: {enlace}"
                lista_tareas.insert(tk.END, tarea)
                ventana_tarea.destroy()

            boton_crear_tarea = tk.Button(ventana_tarea, text="Crear Tarea", command=crear_tarea_reunion)
            boton_crear_tarea.pack(pady=10)

