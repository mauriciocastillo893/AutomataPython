from tkinter import *

raiz = Tk()
raiz.title("Autómata en Python")
# raiz.geometry("500x400")
raiz.resizable(False, False)

# Obtén las dimensiones de la pantalla
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()

x = (ancho_pantalla - 500) // 2  # Ancho de la ventana
y = (alto_pantalla - 500) // 2   # Alto de la ventana

raiz.geometry("500x400+{}+{}".format(x, y))


# Función para establecer el fondo en gris para todos los labels
def set_labels_gray():
    miLabelStatus.config(text="EN ESPERA", bg="gray", font=("Helvetica", 12, "bold italic"))
    # for label in labels:
    for i, label in enumerate(labels):
        label.config(bg="gray", font=("Helvetica", 10, "bold"), pady=0, text=str(i + 1))

def comprobar():
    entrada_texto = entrada.get()
    print(len(entrada_texto))
    set_labels_gray()
    miLabelStatus.config(text="ANALIZANDO...", bg="orange", font=("Helvetica", 12, "bold italic"))
    # labels2 = labels[:-1]
    if len(entrada_texto) == 9:
        confirmarButton.config(state="disabled")
        borrarButton.config(state="disabled")
        label9.config(bg="gray", fg="black", padx=10)
        raiz.after(250, lambda: verificar_primer_caracter())
    elif len(entrada_texto) == 8:
        borrarButton.config(state="disabled")
        confirmarButton.config(state="disabled")
        label9.config(bg="black", fg="black", padx=-100, text="")
        raiz.after(250, lambda: verificar_primer_caracter())
    else:
        print("La longitud de la entrada no es válida, debe ser 8 o 9 de total de caracteres")
        miLabelStatus.config(text="DATOS DEBEN SER MAYORES O IGUALES A 8 DIGITOS", background="red")
    
    # Lógica para el primer carácter (entrada_texto[0])
    def verificar_primer_caracter():
        key_word = 0
        label1.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[0])
        if entrada_texto[0] == 'H':
            print("El primer carácter es 'H', se ha cumplido una condición especial.", entrada_texto[0])
            label1.config(bg="green")
            key_word = entrada_texto[0]
            # Programar el siguiente paso después de 250 ms (1 segundo)
            raiz.after(250, lambda: verificar_segundo_caracter(key_word))
        elif entrada_texto[0] in ('I', 'J'):
            print(f"El primer carácter es '{entrada_texto[0]}', se ha cumplido una condición especial.",entrada_texto[0])
            label1.config(bg="green")
            key_word = entrada_texto[0]
            raiz.after(250, lambda: verificar_segundo_caracter(key_word))
        elif entrada_texto[0] == 'K':
            print("El primer carácter es 'K', se ha cumplido una condición especial.",entrada_texto[0])
            label1.config(bg="green")
            key_word = entrada_texto[0]
            raiz.after(250, lambda: verificar_segundo_caracter(key_word))
        else:
            print("No cumple el primer caracter, especificaciones: "
                    "[H] => U..Z, [I or J] => A...Z, [K] => A...K", entrada_texto[0])
            print("Para poder validar el segundo carácter debemos validar el primero para mayor precisión, por ende, es erroneo por default sin valor del primer carácter para validar al segundo")
            label1.config(bg="red")
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
            # for label in labels2[1:]:
            #     label.config(bg="red") 

    # Lógica para el segundo carácter (entrada_texto[1])
    def verificar_segundo_caracter(key_word):
        print(key_word)
        label1.config(font=("Helvetica", 10, "bold"), pady=0)
        label2.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[1])
        if key_word == 'H':
            print("Entró", key_word)
            for caracter in entrada_texto[1]:
                if 'U' <= caracter <= 'Z':
                    label2.config(bg="green")
                    print(f"El segundo carácter '{caracter}' está en el rango 'U' a 'Z'.")
                    raiz.after(250, lambda: verificar_tercer_caracter())
                else:
                    label2.config(bg="red")
                    print(f"El segundo carácter '{caracter}' no está en el rango 'U' a 'Z'.")
                    borrarButton.config(state="normal")
                    confirmarButton.config(state="normal")
                    miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        elif key_word == 'I' or  key_word == 'J':
            print("Entró", key_word)
            for caracter in entrada_texto[1]:
                if 'A' <= caracter <= 'Z':
                    label2.config(bg="green")
                    print(f"El segundo carácter '{caracter}' está en el rango 'A' a 'Z'.")
                    raiz.after(250, lambda: verificar_tercer_caracter())
                else:
                    label2.config(bg="red")
                    print(f"El segundo carácter '{caracter}' no está en el rango 'A' a 'Z'.")
                    borrarButton.config(state="normal")
                    confirmarButton.config(state="normal")
                    miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        elif key_word == 'K':
            print("Entró", key_word)
            for caracter in entrada_texto[1]:
                if 'A' <= caracter <= 'K':
                    label2.config(bg="green")
                    print(f"El segundo carácter '{caracter}' está en el rango 'A' a 'K'.")
                    raiz.after(250, lambda: verificar_tercer_caracter())
                else:
                    label2.config(bg="red")
                    print(f"El segundo carácter '{caracter}' no está en el rango 'A' a 'K'.")
                    borrarButton.config(state="normal")
                    confirmarButton.config(state="normal")
                    miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        else:
            print("Error Inesperado")
            label2.config(bg="purple")
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    # Lógica para el tercer carácter (entrada_texto[2])
    def verificar_tercer_caracter():
        label1.config(font=("Helvetica", 10, "bold"), pady=0)
        label2.config(font=("Helvetica", 10, "bold"), pady=0)
        label3.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[2])
        if entrada_texto[2] == '-':
            label3.config(bg="green")
            print("El tercer carácter es un guión", entrada_texto[2])
            raiz.after(250, lambda: verificar_cuarto_caracter())
        else:
            label3.config(bg="red")
            print("No cumple el tercer carácter", entrada_texto[2])
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    def verificar_cuarto_caracter():
        label3.config(font=("Helvetica", 10, "bold"), pady=0)
        label4.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[3])

        if entrada_texto[3].isdigit():
            if 1 <= int(entrada_texto[3]) <= 9:
                label4.config(bg="green")
                print("El cuarto carácter está en el rango [1, 9]:", entrada_texto[3])
                raiz.after(250, lambda: verificar_quinto_caracter(1))
            elif int(entrada_texto[3]) == 0:
                label4.config(bg="green")
                print("El cuarto carácter está en el rango [0]:", entrada_texto[3])
                raiz.after(250, lambda: verificar_quinto_caracter(0))
            else:
                label4.config(bg="red")
                print("No cumple el cuarto carácter, debe estar en el rango [0, 9]:", entrada_texto[3])
                borrarButton.config(state="normal")
                confirmarButton.config(state="normal")
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        else:
            label4.config(bg="red")
            print("No cumple el cuarto carácter, debe estar en el rango [0, 9]:", entrada_texto[3])
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    def verificar_quinto_caracter(key_word):
        label4.config(font=("Helvetica", 10, "bold"), pady=0)
        label5.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[4])
        
        quinto_caracter = entrada_texto[4]
        
        # Verifica si el cuarto carácter es un dígito
        if quinto_caracter.isdigit():
            caracter = int(quinto_caracter)  # Convierte el cuarto carácter a un número entero
            if 0 <= caracter <= 9 and key_word == 1:
                label5.config(bg="green")
                print("El quinto carácter está en el rango [0, 9]:", quinto_caracter)
                raiz.after(250, lambda: verificar_sexto_caracter(9))
            elif key_word == 0:
                if caracter == 0:
                    label5.config(bg="green")
                    print("El quinto carácter está en el rango [0]:", quinto_caracter)
                    raiz.after(250, lambda: verificar_sexto_caracter(0))
                elif 1 <= caracter <= 9:
                    label5.config(bg="green")
                    print("El quinto carácter está en el rango [1, 9]:", quinto_caracter)
                    raiz.after(250, lambda: verificar_sexto_caracter(1))
                else:
                    label5.config(bg="red")
                    print("No cumple el quinto carácter, debe estar en el rango [0, 9]:", quinto_caracter)
                    borrarButton.config(state="normal")
                    confirmarButton.config(state="normal") 
                    miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
            else:
                label5.config(bg="red")
                print("No cumple el quinto carácter, debe estar en el rango [0, 9]:", quinto_caracter)
                borrarButton.config(state="normal")
                confirmarButton.config(state="normal")
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        else:
            label5.config(bg="red")
            print("No cumple el quinto carácter, debe estar en el rango de NUMEROS:", quinto_caracter)
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    def verificar_sexto_caracter(key_word):
        label5.config(font=("Helvetica", 10, "bold"), pady=0)
        label6.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[5])
        sexto_caracter = entrada_texto[5]
        print(sexto_caracter)
        # Verifica si el cuarto carácter es un dígito
        if sexto_caracter.isdigit():
            caracter = int(sexto_caracter)  # Convierte el cuarto carácter a un número entero
            if key_word == 9:
                label6.config(bg="green")
                print("El sexto carácter está en el rango [0, 9]:", sexto_caracter)
                raiz.after(250, lambda: verificar_septimo_caracter(9))
            elif key_word == 1:
                label6.config(bg="green")
                print("El sexto carácter está en el rango [0, 9]:", sexto_caracter)
                raiz.after(250, lambda: verificar_septimo_caracter(9))
            elif key_word == 0:
                label6.config(bg="green")
                print("El sexto carácter está en el rango [0]:", sexto_caracter)
                raiz.after(250, lambda: verificar_septimo_caracter(1))
            else:
                label6.config(bg="red")
                print("Fuera de rango:", sexto_caracter)
                borrarButton.config(state="normal")
                confirmarButton.config(state="normal")
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        else:
            label6.config(bg="red")
            print("No cumple el sexto carácter, debe estar en el rango de NUMEROS:", sexto_caracter)
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    def verificar_septimo_caracter(key_word):
        label6.config(font=("Helvetica", 10, "bold"), pady=0)
        label7.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[6])
        septimo_caracter = entrada_texto[6]
        
        # Verifica si el cuarto carácter es un dígito
        if septimo_caracter.isdigit():
            caracter = int(septimo_caracter)  # Convierte el cuarto carácter a un número entero
            if key_word == 1:
                label7.config(bg="green")
                print("El septimo carácter está en el rango [1, 9]:", septimo_caracter)
                raiz.after(250, lambda: verificar_octava_caracter())
            elif key_word == 9:
                label7.config(bg="green")
                print("El septimo carácter está en el rango [0, 9]:", septimo_caracter)
                raiz.after(250, lambda: verificar_octava_caracter())
            else:
                label7.config(bg="red")
                print("Fuera de rango:", septimo_caracter)
                borrarButton.config(state="normal")
                confirmarButton.config(state="normal")
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        else:
            label7.config(bg="red")
            print("No cumple el septimo carácter, debe estar en el rango de NUMEROS:", septimo_caracter)
            borrarButton.config(state="normal")
            confirmarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))

    def verificar_octava_caracter():
        label7.config(font=("Helvetica", 10, "bold"), pady=0)
        label8.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[7])
        
        octavo_caracter = entrada_texto[7]

        if entrada_texto[7] == '-':
            label8.config(bg="green")
            print("El octavo carácter es un guión", entrada_texto[7])
            if len(entrada_texto) < 9:
                label8.config(bg="red")
                label8.config(font=("Helvetica", 10, "bold"), pady=0)
                borrarButton.config(state="normal")
                confirmarButton.config(state="normal")
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
            else:
                raiz.after(250, lambda: verificar_noveno_caracter())
        elif 'A' <= octavo_caracter <= 'Z':
            label8.config(bg="green")
            print(f"El octavo carácter '{octavo_caracter}' está en el rango 'A' a 'Z'.")
            if len(entrada_texto) < 9:
                # label9.config(bg="red")
                label8.config(font=("Helvetica", 10, "bold"), pady=0)
                miLabelStatus.config(text="FINALIZADO SIN ERRORES", bg="green", font=("Helvetica", 12, "bold"))
                # label9.config(pady=2, font=("Helvetica", 14, "bold"), text=entrada_texto[7])
            else:
                label9.config(bg="red")
                label8.config(font=("Helvetica", 10, "bold"), pady=0)
                label9.config(pady=2, font=("Helvetica", 14, "bold"), text=entrada_texto[8])
                miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
            confirmarButton.config(state="normal")
            borrarButton.config(state="normal")
            
        else:
            label8.config(bg="red")
            print(f"No cumple el octavo carácter, debe estar en el rango 'A' a 'Z': {octavo_caracter}")
            confirmarButton.config(state="normal")
            borrarButton.config(state="normal")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))


    def verificar_noveno_caracter():
        label8.config(font=("Helvetica", 10, "bold"), pady=0)
        label9.config(pady=2, font=("Helvetica", 14, "bold italic"), text=entrada_texto[8])
        
        # if len(entrada_texto) < 9:
        #     label9.config(bg="purple")
        #     print("La cadena no tiene 9 caracteres.")

        noveno_caracter = entrada_texto[8]
        
        if noveno_caracter is None:
            label9.config(bg="black", fg="white")
            print("El noveno carácter está vacío.")
        elif 'A' <= noveno_caracter <= 'Z':
            label9.config(bg="green")
            print(f"El noveno carácter '{noveno_caracter}' está en el rango 'A' a 'Z'.")
        else:
            label9.config(bg="red")
            print(f"No cumple el noveno carácter, debe estar en el rango 'A' a 'Z': {noveno_caracter}")
            miLabelStatus.config(text="FINALIZADO CON ERRORES: CARACTER NO ACEPTADO", bg="red", font=("Helvetica", 10, "bold"))
        borrarButton.config(state="normal")
        confirmarButton.config(state="normal")

        miLabelStatus.config(text="FINALIZADO SIN ERRORES", bg="green", font=("Helvetica", 12, "bold"))
        

def on_validate_input(P):
    if len(P) <= 9:
        return True
    else:
        return False
    
def borrar_datos():
    entrada.delete(0, "end")
    set_labels_gray()

# Configurar una variable de control para el Entry
entrada_texto_validacion = StringVar()

# FRAME DE TITULO DEL FRAME1
miFrame=Frame(raiz, width=250, height=100, pady=50)
miFrame.pack(side="top")
Label(miFrame, text="CADENA A EVALUAR", font=("Helvetica", 30, "bold")).grid(row=0, column=0)
Label(miFrame, text="Formato: HU-0001A  hacia  KK-9999-Z", font=("Helvetica", 10, "bold")).grid(row=1, column=0)

# FRAME2 DE MENSAJE DE "CADENA:"
miFrame2=Frame(raiz, width=250, height=100, padx=10)
miFrame2.pack(side="top")
Label(miFrame2, text="Cadena:", fg="black", border="3", bg="orange", font=("Helvetica", 12, "bold")).grid(column=0, row=0)

# ENTRADA DE DATOS
entrada = Entry(miFrame2, textvariable=entrada_texto_validacion, cursor="hand2")
validation = miFrame2.register(on_validate_input)
entrada.config(validate="key", validatecommand=(validation, "%P"), bg="black", fg="orange", insertbackground="orange", font=("Helvetica", 12, "bold"))
entrada.grid(column=1, row=0)

# FRAME3 DE LABELS DE CARGA
miFrame3=Frame(raiz, width=250, height=100, pady=10)
miFrame3.pack(side="top")
label1 = Label(miFrame3, text="1", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label2 = Label(miFrame3, text="2", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label3 = Label(miFrame3, text="3", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label4 = Label(miFrame3, text="4", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label5 = Label(miFrame3, text="5", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label6 = Label(miFrame3, text="6", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label7 = Label(miFrame3, text="7", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label8 = Label(miFrame3, text="8", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label9 = Label(miFrame3, text="9", background="gray", font=("Helvetica", 10, "bold"), padx=10)
label1.grid(column=0, row=0)
label2.grid(column=1, row=0)
label3.grid(column=2, row=0)
label4.grid(column=3, row=0)
label5.grid(column=4, row=0)
label6.grid(column=5, row=0)
label7.grid(column=6, row=0)
label8.grid(column=7, row=0)
label9.grid(column=8, row=0)
labels = [label1, label2, label3, label4, label5, label6, label7, label8, label9]


miFrameText=Frame(raiz, width=250, height=100)
miFrameText.pack(side="top", padx=25, pady=15)
miLabelStatus = Label(miFrameText, text="ESPERANDO CADENA", font=("Helvetica", 12, "bold"), fg="black", border="3", bg="orange")
miLabelStatus.grid(row=1, column=0)


# FRAME4 DE BOTONES
miFrame4=Frame(raiz, width=250, height=100, pady=10)
miFrame4.pack(side="top")
Button(miFrame4, text="Salir", command=raiz.quit, font=("Helvetica", 10, "bold"), bg="red", width=10).grid(row=0, column=0, padx=10, pady=5)
confirmarButton = Button(miFrame4, text="Comprobar", command=comprobar, font=("Helvetica", 10, "bold"), bg="orange", width=10)
confirmarButton.grid(row=0, column=1, padx=10, pady=5)
borrarButton = Button(miFrame4, text="Borrar", command=borrar_datos, font=("Helvetica", 10, "bold"), bg="gray", width=10)
borrarButton.grid(row=0, column=2, padx=10, pady=5)

# FRAME5 Autor
miFrame5=Frame(raiz, width=250, height=100)
miFrame5.pack(side="top", anchor="e", padx=25, pady=5)
Label(miFrame5, text="©CASTILLO 2.0v", font=("Helvetica", 7, "bold")).grid(row=1, column=0)


raiz.mainloop()
