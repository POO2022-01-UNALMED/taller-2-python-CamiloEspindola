from email.errors import MalformedHeaderDefect
from enum import auto
from re import T
from shutil import RegistryError
from socket import MSG_DONTROUTE


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor (self, color):
        if(color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color
            
class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca 
        self.motor = motor 
        self.registro = registro
        Auto.cantidadCreados+=1
        
    def cantidadAsientos(self):
        if len(self.asientos)>0:
            c=0
            for i in self.asientos:
                if isinstance(i,Asiento):
                    c+=1
        else:
            return(0)
        return(c) # debe ser number
    
    def verificarIntegridad(self):
        if isinstance(self.motor, Motor):
            registro= self.motor.registro
            if registro==self.registro:
                if len(self.asientos)>0:
                    for i in self.asientos:
                        if isinstance(i,Asiento):
                            if registro!=i.registro:
                                registro= False       
            else:
                registro= False

            if not registro:
                return "Las piezas no son originales"
            else:
                return "Auto original"
                
        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro=registro
    
    def asignarTipo(self, tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo