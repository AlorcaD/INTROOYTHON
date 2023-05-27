"""
interger y float 
numeros acompañados de esta forma in (3, 4, 5) dentro de un parentesis son
tuplas.
los decimales se separan por puntos las comas genera un numero aparte.
operaciones aritméticas:
adicion +
sustraccion -
multiplicacion *
division /   cualquier numero dividido por 0 genera error.
potencia **
resto modulo %

"""


"""
las variables como su nombre lo dice son elementos que varían
significa que pueden tener diversos valores en diversos momentos.
 #TIEMPO DE RECUPERACION DE UNA INVERSION EN AÑOS
 
"""
#nversionTotal = 1000
#ngresoAnual = 100
#rint(inversionTotal / ingresoAnual)
#10.0



#inversonInicial = 1000
#tiempoDeRetorno = 5
#ingresosAnuales = inversionInicial/tiempoRetorno
#print(ingresosAnuales)
#200.0

#cantidadInvertida = 2500
#añosDeRecuperacion = 3
#ingresosAnuales = cantidadInvertida / añosDeRecuperacion
#print(ingresosAnuales)
#b 833


"""
Int Float Str para que sirven: uso puramente computacional ya que determinan el formato
de como se debe interpretar, es util saberlo ya que hay operaciones que 
se pueden ver restringidas por el tipo de dato.
tambien nos ayuda a identificar tipos de datos mas complejos.
como listas, arreglos, tuplas, booleanos
"""

"""
Cadenas String en python Str CREADA AL ESCRIBIR un "textoEntreComillas" 'simplesODobles'
algunos caracteres para ser impresos deben llevar un  \ ejemplo 'jorge\'s house'
"""
#print(' Jorge\'s Hosue')

"""
Las Cadenas pueden ser sumadas o unidas con el simbolo + se conoce como concatenación
no importa que tipo de comilla y funciona con cadenas vacias para generar espacios.
"""
   #print("cadenas" + 'vacias')
#cadenasvacias
   #print("cadenas" + ' ' + "vacias")
#cadenas vacias

"""
tambien se puede concatenar numeros "3" si estos van entre comillas '3'
"""
   #print('2' + "4")
#24

"""
pero no se puede sumar un numero a una cadena porque son tipos de datos
distintos ejemplo 10 + "10"

en caso de multiplicar si es posible multiplicando el texto 
"hola" * 3 
out : holaholahola

ninguna otra operacion artimetica funciona de esta forma.
"""

#print("21" * 4 )
#21212121

"""
COMENTAR EL CODIGO ES SIEMPRE NECESARIO. PARA LOS DEMAS QUE LEAN TU CODIGO.
#COMO PARA LA VERSION TUYA DEL FUTURO
"""

#LISTAS O TUPLAS no entiendo el type nunca arroja el dato

   #lista = [1, 3, 5, 7]
   #print(lista[0])
     #tupla = (2, 4, 5 ,6 ,7 )
     #type(tupla)


"""
los datos listas tiene propiedad muy utiles, 
nos da la opcion de : indicar la posicion de un elemento dentro de la lista
a esto se le llama INDEXAR
.remove sirve para remover un objeto de la lista
.append sirve para agregar al final de la lista un objeto
.pop sirve para quitarle elementos(no me sirvio )
"""

   #lista = ['objeto 1', 'objeto 2', 'objeto 3', 'objeto 4']
   #lista.append("objeto 5")
   #print(lista)
       #['objeto 1', 'objeto 2', 'objeto 3', 'objeto 4', 'objeto 5']


"""
VALORES LOGICOS INENTIFICADOS COMO "BOOL" DE BOOLEANOS
este tipo de valores representan reglas de la logica, expresada
en la evaluación de enunciados como verdaderos o falsos.

"""
#EN LA TABLA SE RESUMEN LOS SIMBOLOS Y SUS EJEMPLO CON OPERADORES DE COMPARACION
"""
Menor que < 3 < 5 true evalua si el valor izquiero es menor al derecho
Mayor que > 4 > 6 false evalua si el valor izquier es mayor al derecho
Igual que == 2.01 == 2 false evalua si dos terminos son igual igualdad exacta
Menor o = que < 4 <= 4 true evalua si el val izq es menor o igual al derecho
Mayor o = que > 5 >= 5 true evalua si el val izq es mayor o igual al derecho
Distinto de != 9 != 9 false evalua si untermino es distinto de otro
"""
# TRUE O FALSE SON EXPRESIONES PROPIAS DE PYTHON
#PODEMOS GENERAR ESTE TIPO DE VARIABLES

   #verdadera = (2 + 3 != 5)
  #print(verdadera)

"""EXISTE UN TIPO ESPECIAL DE OPERADORES LOGICOS QUE PERMITEN TRABAJAR
EXPRESIONES MAS COMPLEJAS DE LOGICA, COMO SON LAS PROPOSICIONES
COMPUESTAS, CUYA DINAMICA SE PUEDE REPRESENTAR EN TABLAS DE VERDAD,
COMO LAS SIGUIENTES"""

#AND 
#PROPOSICION 1     PROPOSICION 2    CONCLUSION
#TRUE               TRUE                TRUE
#TRUE               False               FALSE
#FALSE              TRUE                FALSE
#FALSE              FALSE               FALSE

#OR
#PROPOSICION 1     PROPOSICION 2    CONCLUSION
#TRUE               TRUE                TRUE
#TRUE               FALSE               TRUE
#FALSE              TRUE                TRUE
#FALSE              FALSE               FALSE

#NOT
#PROPOSICION        NEGACION
#TRUE               FALSE
#FALSE              TRUE


"""EJEMPLOS
USO DE AND
"""
"""
proposicion1 = (2 + 2 ==4)
proposicion2 = true
proposicion1 and proposicion2
true
true and true = true
proposicion1 = 3 < 1
proposicion2 = 3 > 1
proposicion1 and proposicion 2
false
true and false = false
"""
"""
USO DE OR
proposicion1 = 3 ** 2 == 9
proposicion2 = 2 + 2 == "pez"
proposicion1 or proposicion2
true
true or false = true
usando or una sentencia es falasa si ambas son falsas

proposicion1 = 'Hola' == 'hola'
proposicion = 'Adios' == 'adios'
proposicion1 or proposicion2
false

las cadenas son sensibles a las mayusculas ambas son falsas
false or false = false

en el caso de NOT
INVIERTE EL RESULTADO NOT TRUE = FALSE NOT FALSE = TRUE

proposicion1 = (2 + 2 ==4)
proposicion2 = true
not proposicion1 and proposicion2
true false

los datos booleanos para la maquina son numero 0 Y 1 Y se pueden aplicar
operaciones artimeticas en estos 
true + true + true.
"""

#OBJETOS (1)
#LOS OBJETOS SON LAS INSTANCIAS DE UNA CLASE, LAS CUALES SON LA REPRESENTACION
#O ABSTRACCION DE UN ELEMENTO DE LA REALIDAD.



#class perro:
  #  ladrar = "Guau!"
   # aullar = "Auuuuu!"

    #print(perro.ladrar)
    #print(perro.aullar)
#Guau!
#Auuuuu!


#variable = perro

#variable.aullar
#print(variable.aullar)

#class perro:
 #   ladrar = "Guau!"
  #  aullar = "Auuuuu!"
    
    
#englishDog = perro
#englishDog.ladrar = "Woof", "woof"
#perro.ladrarFrances = "waan"
#perro.ladrarJapones = "woaufes"

#print(perro.ladradjapones)
#woaufes

"""
Objetos 3 por ultimo una clase tambien puede tener 
elemento mas complejos como funciones.
llamados metodos de contexto de clase.
pondremos una funcion que sume 2 valores dentro de la clase y la llamamos
desde el objeto 
"""

#class operacion:
 #   def sumar(x, y):
 #       print(x + y)
#operacion.sumar(2, 2)

     
"""SINTESIS DE TIPOS DE DATOS
ENTERO = INTEGER
FLOTANTES = FLOAT
CADENAS = STR
LISTAS = LIST
BOOLEANOS = BOOL
OBJETOS = TYPE


#AHORA COMENZAMOS CON LAS FUNCIONES
"""

#FUNCION MECANISMO QUE RECIBE UNO O VARIOS PARAMETROS DE ENTRADA
#input para los cuales define una serie de procedimiento u operaciones y genera
#un resultado.
#asi la funcion Print recibe como Input una variable, la cual convierte
#en algo visible para la consola y finalmente lo visualiza en la pantalla.
#DADO ELLO TENEMOS FUNCIONES DE TODO TIPO
#EJEMPLO

#X = sum([2, 2, 2])
#print(X)

#Por ejemplo, podemos tener una función que solo imprima un valor, así

#def buenos_dias():
 #   print("buenos días")
    
"""lista = [2, 3, 4, 5, 6, 7]
print(max(lista))
print(min(lista))
print(len(lista))
"""

"""DEFINIR UNA FUNCION"""

"""PARA CREAR UNA FUNCION PYTHON SE USA EL COMANDO DEF Y EL NOMBRE DE LA FUNCION
PARENTESIS Y UN PARAMETRO DENTRO DEL PARENTISIS Y DOS PUNTOS"""

#FUNCION QUE EVALUA UN RESTO

#def esPar(numero):
#    print(numero % 2 == 0)
  #identacion  

"""Debajo del nombre de la función, hemos dejado un espacio, el cual es obligatorio ya que es una propiedad de la sintaxis de 
Python, y se le conoce como indentación. Posteriormente, al aplicar otras estructuras, como las iteraciones o los 
condicionales anidados, se requerirá especial atención a la indentación.
"""

#def esPar(numero):
 #   return numero % 2 == 0    


#def retorno(cantidadInvertida, ingresosAnuales):
#    return cantidadInvertida/ingresosAnuales
 
#import random
#random.random()  
   
#import random as rd
#rd.random()

"""LIBRERIAS
LAS LIBRERIAS EMPAQUETAN UNA SERIE DE FUNCIONALIDADES PARA DISTINTO FINES.
EN ESTE CURSO USAREMOS VARIAS LIBRERIAS QUE PRESENTAREMOS EN LAS PROXIMAS SESIONES

COMO GENERAR NUMERO ALEATORIOS
import random
TAMBIEN PODEMOS GENERAR NUESTRO PRIMER NUMERO ALEATORIO
random.random() 
POR OTRO LADO PODEMOS IMPORTAR LIBRERIAS CON ALIAS O APODOS HACIENDO MAS AGIL EL USO
import random as rd
rd.random()
LA LIBRERIAS OPERA COMO OBJETO CLASE RANDOM PERMITIENDO LLAMAR SUS METODOS O FUNCIONES.

ES COMUN QUE LAS LIBRERIAS TENGAN MAS DE UN MODULO
POR LO QUE SI VAMOS A USAR UN COMPONENTE ESPECIFICO, DEBEMOS SEÑALARLO

EJEMPLO
SI QUEREMOS IMPRIMIR LA FECHA Y EL DÍA LO HACEMOS CON EL MODULO DATE DE LA 
LIBRERIA DATETIME
"""

#from DATETIME import DATE as dt
#dt.today()
#datetime.date(2023, 05,26)





#
#
#S3S10N 4
#condiciona dentro de la funcion por medio de las sentencias.

#if True:
#    print("esto es verdadero")
#else:
#    print("esto es falso")
#esto es verdadero

#if 2 + 2 < 2:
#    print("esto es verdadero")
#else:
#    print("esto es falso")
#esto es falso



"""
def esPar(numero):
    if numero % 2 == 0:
        print("es par")
    else:
        print("no es par")
esPar(12)
es par
"""

#def esImpar(numero):
#    if numero % 2 != 0:
#        print("Es impar")
#    else:
 #       print("es par")

#esImpar(3)
#Es impar



#Condicionales anidados

#def esPar3(x, texto=False):
#    if x % 2 == 0:
#        if texto:
#            print("Es par")
#        else:
#            return True
#    else:
#        if texto:
#            print("es impar")
#        else:
#            return False

"""
def funcion(x):
    if x % 2 == 0:
        if x % 3 == 0:
            print("hola")
        else:
            print("adios")
    else:
        print("que te vaya bien")        
"""

"""# USANDO FOR
lista = ["arroz", "ajo", "sal", "aceite"]
for i in lista:
    print(i)
arroz
ajo
sal
aceite
"""


    #USANDO WHILE


lista = ["arroz", "ajo", "sal", "aceite"]
i = 0 
cantidadElemento = len(lista)

while(i != cantidadElemento):
    print(lista[i])
    i += 1


 ESTO ES UN BUCLE INFINITO
while(True):
    print("hola")


lista = ["arroz", "ajo", "sal", "aceite"]
for i in range(0, 3):
    print(lista[i])


lista = ["arroz", "ajo", "sal", "aceite"]
for i in range(0, len(lista)):
    print("el indice " + str(i) + " " + "posee el objeto: " + lista[i])



""" # 5TA Y ULTIMA SESION VAMOS
"""















