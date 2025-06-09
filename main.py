import tkinter as tk
import random
import copy
from tkinter import messagebox

# Funcion encargada de actualizar las etiquetas de puntaje, intentos y palabra en la ventana del juego
#E: Dos numeros enteros (puntaje y la cantidad de intentos restantes)
#S: Etiquetas con valores actualizados en la ventana del juego
#R:
def actualizar_etiquetas(puntaje,intentos):
    global etiqueta_uno
    global etiqueta_dos
    global etiqueta_tres
    etiqueta_uno.config(text="Puntaje: "+str(puntaje))
    etiqueta_dos.config(text="Intentos: "+str(intentos))
    etiqueta_tres.config(text="Palabra: ")

    etiqueta_uno.update()
    etiqueta_dos.update()
    etiqueta_tres.update()

# Funcion encargada de actualizar palabra que estamos armando en la ventana del juego
#E: La palabra con un nuevo caracter para actualizar en la ventna del juego
#S: Palabra actualizada en la ventna del juego
#R:
def actualizar_etiqueta_palabra(palabra_seleccionada):
    global etiqueta_tres
    etiqueta_tres= tk.Label(text="Palabra: "+"".join(palabra_seleccionada), font=("Arial",12))
    etiqueta_tres.grid(column=14,row=3)
    etiqueta_tres.update()
    
# Funcion encargada de leer un archivo de texto con el banco de palabras a colocar en la matriz
#E: N/A
#S: Una cadena de texto con la informacion del archivo que leimos
#R: 
def leer_entrada_de_texto():
    archivo = open("palabras.txt")
    return(archivo.read())

# Funcion encargada de revisar la longitud de cada una de las palabras de la lista y obtener la longitud maxima
#E: Una lista de palabras (string)
#S: Un numero entero que indica la longitud de la palabra mas grnade de la lista de palabras
#R:
def longitud_maxima_de_palabra(lista_de_palabras):
    cantidad_de_letras=0
    for palabra in lista_de_palabras:
        if len(palabra)>cantidad_de_letras:
            cantidad_de_letras=len(palabra)
    return(cantidad_de_letras)
    
# Funcion encargada de generar una matriz de nxn con el caracter "_" como valor por defecto
#E: Un numero entero positivo (tamano de la matriz cuadrada)
#S: Una matriz de nxn con el caracter "_" por defecto en todas las posiciones
#R:
def generar_matriz_logica(longitud_maxima):
    matriz = [["_" for i in range(longitud_maxima)] for j in range(longitud_maxima)]
    return(matriz)

# Funcion encargada de verificar si una palabra puede colocarse en orientacion izquierda-derecha en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
#R:
def validar_izquierda_derecha(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x+longitud_de_palabra > longitud_maxima):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x+campo][eje_y]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion izquierda-derecha
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:            
def agregar_izquierda_derecha(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x+desplazamiento][eje_y] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion derecha-izquierda en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_derecha_izquierda(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x-longitud_de_palabra < 0):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x-campo][eje_y]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion derecha-izquierda
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:              
def agregar_derecha_izquierda(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x+desplazamiento][eje_y] = letra
        desplazamiento = desplazamiento-1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion arriba-abajo en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_arriba_abajo(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_y+longitud_de_palabra > longitud_maxima):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x][eje_y+campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion arriba-abajo
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:             
def agregar_arriba_abajo(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x][eje_y+desplazamiento] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion abajo-arriba en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_abajo_arriba(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_y-longitud_de_palabra < 0):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x][eje_y-campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion abajo-arriba
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:             
def agregar_abajo_arriba(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x][eje_y+desplazamiento] = letra
        desplazamiento = desplazamiento-1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion diagonal hacia abajo de izquierda a derecha en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_diagonal_abajo_izq_der(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x+longitud_de_palabra > longitud_maxima)or(eje_y+longitud_de_palabra > longitud_maxima):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x+campo][eje_y+campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion diagonal hacia abajo de izquierda a derecha
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:            
def agregar_diagonal_abajo_izq_der(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x+desplazamiento][eje_y+desplazamiento] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion diagonal hacia arriba de izquierda a derecha en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_diagonal_arriba_izq_der(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x+longitud_de_palabra > longitud_maxima)or(eje_y-longitud_de_palabra < 0):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x+campo][eje_y-campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion diagonal hacia arriba de izquierda a derecha
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:             
def agregar_diagonal_arriba_izq_der(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x+desplazamiento][eje_y-desplazamiento] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion diagonal hacia abajo de derecha a izquierda en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_diagonal_abajo_der_izq(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x-longitud_de_palabra < 0)or(eje_y+longitud_de_palabra > longitud_maxima):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x-campo][eje_y+campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion diagonal hacia abajo de derecha a izquierda
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:            
def agregar_diagonal_abajo_der_izq(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x-desplazamiento][eje_y+desplazamiento] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de verificar si una palabra puede colocarse en orientacion diagonal hacia arriba de derecha a izquierda en (x,y)
#E: Matriz, la palabra que queremos insertar, puntos iniciales (x,y) y la longitud de la matriz
#S: Retorna True si la palabra se puede insertar, False caso ocntrario
def validar_diagonal_arriba_der_izq(matriz, palabra, eje_x, eje_y,longitud_maxima):
    longitud_de_palabra = len(palabra)
    if (eje_x-longitud_de_palabra < 0)or(eje_y-longitud_de_palabra < 0):
        return False
    else:
        for campo in range(0,longitud_de_palabra):
            if matriz[eje_x-campo][eje_y-campo]!= "_":
                return False
        return True

# Funcion encargada de insertar una palabra en la matriz en orientacion diagonal hacia arriba de derecha a izquierda
#E: Una matriz, la palabra que deseamos insertar y los puntos iniciales
#S: La matriz actualizada
#R:            
def agregar_diagonal_arriba_der_izq(matriz, palabra, eje_x, eje_y):
    desplazamiento = 0
    for letra in palabra:
        matriz[eje_x-desplazamiento][eje_y-desplazamiento] = letra
        desplazamiento = desplazamiento+1
    return matriz

# Funcion encargada de generar y de llamar de forma aleatoria las funciones que se encargaran de verificar y agregar las palabras en la matriz
#E: La matriz de palabras, la lista de palabras que debemos agregar, y la longitud de la matriz (en este caso siempre sera de nxn)
#S: La matriz con todas las palabras agregadas de forma aleatoria en la matriz
#R:
def colocar_palabras_en_matriz(matriz, lista_de_palabras, longitud_maxima):
    for palabra in lista_de_palabras:
        palabra_agregada_a_la_matriz=False
        while not palabra_agregada_a_la_matriz:
            orientacion= random.randint(1, 8)
            eje_x= random.randint(0, longitud_maxima-1)
            eje_y= random.randint(0, longitud_maxima-1)
            match orientacion:
                case 1:
                    palabra_agregada_a_la_matriz=validar_izquierda_derecha(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_izquierda_derecha(matriz, palabra, eje_x, eje_y)
                    
                case 2:
                    palabra_agregada_a_la_matriz=validar_derecha_izquierda(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_derecha_izquierda(matriz, palabra, eje_x, eje_y)
                    
                case 3:
                    palabra_agregada_a_la_matriz=validar_arriba_abajo(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_arriba_abajo(matriz, palabra, eje_x, eje_y)
                    
                case 4:
                    palabra_agregada_a_la_matriz=validar_abajo_arriba(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_abajo_arriba(matriz, palabra, eje_x, eje_y)
                    
                case 5:
                    palabra_agregada_a_la_matriz=validar_diagonal_abajo_izq_der(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_diagonal_abajo_izq_der(matriz, palabra, eje_x, eje_y)
                    
                case 6:
                    palabra_agregada_a_la_matriz=validar_diagonal_arriba_izq_der(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_diagonal_arriba_izq_der(matriz, palabra, eje_x, eje_y)
                    
                case 7:
                    palabra_agregada_a_la_matriz=validar_diagonal_abajo_der_izq(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_diagonal_abajo_der_izq(matriz, palabra, eje_x, eje_y)
                    
                case 8:
                    palabra_agregada_a_la_matriz=validar_diagonal_arriba_der_izq(matriz, palabra, eje_x, eje_y,longitud_maxima)
                    if palabra_agregada_a_la_matriz:
                        matriz = agregar_diagonal_arriba_der_izq(matriz, palabra, eje_x, eje_y)
                    
    return matriz                

# Funcion encargada de rellenar los espacios vacios en la matriz con letras de forma aleatoria
#E: La matriz de nxn
#S: La matriz con todas las letras actualizadas
#R:
def rellenar_Matriz_letras_aleatorias(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz)):
            if matriz[i][j]== "_":
                matriz[i][j] = random.choice("abcdefghijklmnopqrstuvwxyz")
    return matriz

# Funcion encargada de guardar el caracter y la posicion de este en las listas posiciones y palabra_seleccionada.
#E: Posicion (fila y columna) y el caracter
#S: Lista de posiciones y palabra actualizadas, ventana del juego actualizada
#R:
def accion_boton_matriz(eje_x,eje_y,valor):
    global posiciones
    global palabra_seleccionada
    posiciones.append([eje_x, eje_y])
    palabra_seleccionada.append(valor)
    actualizar_etiqueta_palabra(palabra_seleccionada)

# Fucnion encargada de colocar en la ventana del juego el banco dse palabras del juego
#E: La lista de palabras que fue insertada en la sopa de letras
#S: Banco de palabras visible en la ventana del juego
#R:
def banco_de_palabras(lista_de_palabras):
    tk.Label(palabras, text="Banco de palabras:").pack()
    for p in lista_de_palabras:
        tk.Label(palabras, text=p).pack()

# Funcion encargada de actualizar el aspecto de los botones que estan relacionados a la palabra que seleccionamos
#E: N/A
#S: Propiedades de los botones de la sopa de letras actualizados
#R:
def marcar_botones():
    global posiciones
    global lista_botones
    global longitud_maxima
    
    for posicion in posiciones:
        lista_botones[longitud_maxima*posicion[0]+posicion[1]].config(bg="black", fg="red")
        lista_botones[longitud_maxima*posicion[0]+posicion[1]].update()
    
# Funcion encargada de verificar la palabra contra el banco de palabras y actualizar la sopa de letras. 
# Tambien se encarga de actualizar el puntaje y verificar la cantidad de intentos.
#E: N/A
#S: Puntaje e intentos actualizados si la palabra es correcta o no, finalizacion del juego si excede los intentos o el banco esta vacio
#R:
def verificar_palabra():
    global palabra_seleccionada
    global posiciones
    global puntaje
    global intentos
    global lista_de_palabras
    global root
    es_correcta = False
    for palabra_en_banco in lista_de_palabras:
        if palabra_en_banco == "".join(palabra_seleccionada):
            es_correcta = True
            lista_de_palabras.remove(palabra_en_banco)
            tk.Label(palabras, text=palabra_seleccionada).pack()
            marcar_botones()
            break

    if es_correcta:
        puntaje = puntaje + 10
        tk.Label(palabras, text=palabra_seleccionada).pack
    else:
        intentos= intentos-1

    palabra_seleccionada = []
    posiciones =[]
    actualizar_etiquetas(puntaje,intentos)

    if len(lista_de_palabras)==0:
        print("HAS GANADO...!! :) :) (: (:")
        messagebox.showinfo("Ganaste", "HAS GANADO...!! :) :) (: (:")
        root.destroy()
    elif intentos == 0:
        for i in range(0,longitud_maxima):
            for j in range(0,longitud_maxima):
                if matriz_sol[i][j]!="_":
                    lista_botones[longitud_maxima*i+j].config(bg="black", fg="red")
                    lista_botones[longitud_maxima*i+j].update()
        print("HAS PERDIDO...!! :( :( ): ):")
        messagebox.showinfo("PERDISTE", "HAS PERDIDO...!! :( :( ): ):")
        root.destroy()

# Funcion encargada de finalizar el juego y mostrar al usuario la solucion de la sopa
#E: N/A
#S: Fin del juego
#R:
def rendirse():
    global root
    global matriz_sol
    global lista_botones
    global longitud_maxima
    for i in range(0,longitud_maxima):
        for j in range(0,longitud_maxima):
            if matriz_sol[i][j]!="_":
                lista_botones[longitud_maxima*i+j].config(bg="black", fg="red")
                lista_botones[longitud_maxima*i+j].update()
    messagebox.showinfo("PERDISTE", "HAS PERDIDO...!! :( :( ): ):")
    print ("FIN DEL PROGRAMA, GRACIAS POR JUGAR..!!!! :)")
    root.destroy()
    
#------------------------------------------- Inicio del codigo------------------------------
# Generacion de la parte logica del juego
puntaje = 0
intentos = 3
posiciones=[]
palabra_seleccionada=[]
matriz_sol=[]
lista_botones=[]

palabras_string = leer_entrada_de_texto()
lista_de_palabras = palabras_string.split('\n')
if len(lista_de_palabras)>0 and len(lista_de_palabras)<=10: 
    longitud_maxima = longitud_maxima_de_palabra(lista_de_palabras)

    matriz = generar_matriz_logica(longitud_maxima)
    matriz = colocar_palabras_en_matriz(matriz, lista_de_palabras, longitud_maxima)
    matriz_sol = copy.deepcopy(matriz)
    matriz = rellenar_Matriz_letras_aleatorias(matriz)

#-------------------------------- Aqui comienza el desarrollo de la parte grafica del juego-----------------------

    root = tk.Tk()
    root.title("Sopa de Letras")
    root.geometry("950x800")  # Ancho x Alto
    root.config(padx=35,pady=35)


    # Frame para el tablero (izquierda)
    tablero = tk.Frame(root)
    tablero.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_uno= tk.Label(text="Puntaje: "+str(puntaje), font=("Arial",12))
    etiqueta_uno.grid(column=14,row=1)

    etiqueta_dos= tk.Label(text="Intentos: "+str(intentos), font=("Arial",12))
    etiqueta_dos.grid(column=14,row=2)

    etiqueta_tres= tk.Label(text="Palabra: "+"".join(palabra_seleccionada), font=("Arial",12))
    etiqueta_tres.grid(column=14,row=3)

    # Frame para la lista de palabras (derecha)
    palabras = tk.Frame(root)
    palabras.grid(row=0, column=1, padx=10, pady=10)

    # Llenar el tablero con botones
    for fila in range(longitud_maxima):
        for col in range(longitud_maxima):
            boton = tk.Button(tablero, text=matriz[fila][col], command=lambda f=fila,c=col,v=matriz[fila][col]: accion_boton_matriz(f,c,v) , width=6, height=3)
            boton.grid(row=fila, column=col)
            lista_botones.append(boton)

    # Lista de palabras en el otro frame
    banco_de_palabras(lista_de_palabras)

    tk.Button(palabras,text="Verificar", command=lambda :verificar_palabra()).pack()
    tk.Button(palabras,text="Rendirse",  command=lambda :rendirse()).pack()

    tk.Label(palabras, text="Palabras encontradas: ").pack()



    root.mainloop()
else:
    messagebox.showinfo("ERROR", "La cantidad de palabras en el archivo debe ser entre 1 y 10")
