#Programa que calcula la longitud de una palabra
print("  ______________________________________________________\n")
print("|\tCALCULA LA LONGITUD DE UNA PALABRA")
print("  ______________________________________________________")
#creamos una funcion llamada val_p para validar si son letras lo que esta ingresando 
def val_p():
    return palabra
while True: 
    #Le pedimos al usuario que ingrese una palabra y lo guardamos en la variable palabra
    palabra = input("| Ingrese una palabra que tenga entre 4 a 8 letras : " )
    #validamos si la cadena es alfabetica y si no mostrar un mensaje
    if palabra.isalpha() :
        break
    else:
        print("| Error es un numero o esta vacio")    
#Fin de la funcion
#llamamos ala funcion val_p()
val_p()
#validamos la longitud de la palabra con la funcion len y posteriormente su respectivo mensaje
if len(palabra) <= 3:
    print(f"| Su palabra fue : {palabra} y tiene {len(palabra)} letras \n | Le hace falta letras")
elif len(palabra) >= 4 and len(palabra) <= 7 :
    print(f"| Su palabra fue : {palabra} y tiene {len(palabra)} letras \n | Su palabra es correcta")
elif len(palabra) > 7:
    print(f"| Su palabra fue : {palabra} y tiene {len(palabra)} letras \n | Le sobran letras")
#Fin del primer programa
#Programa que menciona en que cuadrante estas del plano por los ejes del sistema cartesiano
print("  ______________________________________________________\n")
print("|\tENCUENTRA EL CUADRANTE")
print("  ______________________________________________________")
#creamos una funcion llamada val_x para validar si es un numero lo que esta ingresando 
def val_x():
    return x
while True: 
    try:
        #Le pedimos al usuario que ingrese su altura y lo guardamos en la variable altura
        x = int(input("| Ingrese un numero entero sea + o - en el eje de las X: " ))
        break     
    except ValueError:
            print("| Error no es un numero ingresar nuevamente")
#Fin de la funcion
#creamos una funcion llamada val_y para validar si es un numero lo que esta ingresando 
def val_y():
    return y
while True: 
    try:
        #Le pedimos al usuario que ingrese su altura y lo guardamos en la variable altura
        y = int(input("| Ingrese un numero entero sea + o - en el eje de las Y: " ))
        break       
    except ValueError:
            print("| Error no es un numero ingresar nuevamente")
#Fin de la funcion
#mandamos a llamar a las funciones
val_x()
val_y()
#validamos en en cuadrante de encuentra
if x == 0 and y == 0:
    print("| Estan en el origen")
elif x > 0 and y > 0:
    print("| Esta en el cuadrante I")
elif x < 0 and y > 0:
    print("| Esta en el cuadrante II")
elif x < 0 and y < 0:
    print("| Esta en el cuadrante III")
elif x > 0 and y < 0:
    print("| Esta en el cuadrante IV")
elif x == 0 and y > 0 or y < 0:
    print("| Esta en el eje Y")
elif x > 0 or x < 0 and y == 0:
    print("| Esta en el eje X") 
#Fin del programa