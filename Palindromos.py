import tkinter as tk
from tkinter import messagebox

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Función para encontrar todos los palíndromos en una cadena
def encontrar_palindromos(cadena):
    longitud = len(cadena)
    palindromos = set()
    
    # Explorar todas las subcadenas de 'cadena'
    for i in range(longitud):
        for j in range(i + 2, longitud + 1):  # Subcadenas de longitud >= 2
            subcadena = cadena[i:j]
            if es_palindromo(subcadena):
                palindromos.add(subcadena)
    
    return list(palindromos)

# Función para manejar la entrada y salida de la máquina
def procesar_cadena():
    entrada = entry.get()
    
    # Validar que la entrada es numérica
    if not entrada.isdigit():
        messagebox.showerror("Error", "Por favor ingrese una cadena numérica válida.")
        return
    
    # Obtener palíndromos
    palindromos = encontrar_palindromos(entrada)
    
    # Mostrar resultados
    if palindromos:
        resultado = "Palíndromos encontrados: " + ", ".join(palindromos)
    else:
        resultado = "No se encontraron palíndromos en la cadena."
    
    output_label.config(text=resultado)

# Configuración de la interfaz gráfica con tkinter
root = tk.Tk()
root.title("Máquina de Turing: Detector de Palíndromos")
root.geometry("400x300")
root.configure(bg="#333333")

# Estilos
estilo_boton = {"bg": "black", "fg": "white", "font": ("Helvetica", 12), "relief": "flat", "bd": 0}
estilo_input_output = {"bg": "#ffffff", "fg": "#000000", "font": ("Helvetica", 12), "relief": "flat", "highlightthickness": 1, "highlightbackground": "#555555"}

# Crear el campo de entrada con bordes redondeados
entry = tk.Entry(root, **estilo_input_output)
entry.place(x=50, y=50, width=300, height=40)
entry.config(borderwidth=5)

# Botón para aceptar la entrada
aceptar_btn = tk.Button(root, text="Aceptar", command=procesar_cadena, **estilo_boton)
aceptar_btn.place(x=150, y=110, width=100, height=40)

# Etiqueta de salida para mostrar los resultados
output_label = tk.Label(root, text="", **estilo_input_output, wraplength=280, justify="center")
output_label.place(x=50, y=180, width=300, height=80)

# Estilo redondeado
def hacer_redondeado(widget):
    widget.config(highlightbackground="#000000", highlightthickness=2)

hacer_redondeado(entry)
hacer_redondeado(output_label)

root.mainloop()
