# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:35:11 2023

@author: aaron
"""

#jugada de la maquin
def maquina():
    jugada = rd.randrange(0, 3)
    if jugada == 0:
        return "piedra"
    if jugada == 1:
        return "papel"
    if jugada == 2:
        return "tijeras"
    
    
    #capacidad de interaccion con la maquina
def match(jugada):
    python = maquina()
    
    print("python jugó: " + python)
    
    if jugada == python:
        return 0
    if jugada == "piedra" and python == "tijera":
        return 1
    if jugada == "piedra" and python == "papel":
        return -1
    if jugada == "papel" and python == "piedra":
        return 1
    if jugada == "papel" and python == "tijera":
        return -1
    if jugada == "tijera" and python == "papel":
        return 1
    if jugada == "tijera" and python == "piedra":
        return -1
    
    #simulacion de rondas
    rondas = 3
    resultado = list()
    for i in range(0, rondas):#se elimina esta linea ya que ira como parametro
        jugador = input()
        resultado = match(jugador)
        resultado.append(resultado)
     
        #definicion de resultados
     
    if sum(resultado) == 0:
        print("empate")
    if sum(resultado) > 0:
        print("ganaste")
    if sum(resultado) < 0:
        print("perdiste")
        
        
        
def cachipun(rondas = 1):
    resultados = list()
    
    for i in range(0, rondas):
        print("ronda: #" + str(i+1))
        print("ingrese su juego [piedra, papel, o tijeras]")
        jugador = input()
        resultado = match(jugador)
        resultados.append(resultado)
        print("========================")
        
    print("RESULTADO:")    
    if sum(resultado) == 0:
        print("empate")
    if sum(resultado) > 0:
        print("ganaste")
    if sum(resultado) < 0:
        print("perdiste")
        
def aLaPrimera():
    resultado = 0
    
    print("ingrese su juego [piedra, papel, o tijera]")
    
    while(resultado == 0):
    
        jugador = input()
    
        resultado = match(jugador)
        print("========================")
   print("resultado: ")
   if resultado > 0:
       print("ganaste")
   else:
       print("perdiste")
       
       