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
    def __init__(self, modelo, precio, asiento, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asiento = asiento
        """if isinstance(asiento, list):
            if len(asiento)>0:
                for i in asiento:
                    if not isinstance(i,Asiento):
                        raise Exception("Uno de los elementos de asientos ")"""
        self.marca = marca 
        self.motor = motor 
        self.registro = registro 
        self.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        if len(self.Asiento)>0:
            c=0
            for i in self.asiento:
                if isinstance(i,Asiento):
                    c+=1
        else:
            return(0)
        return(c) # debe ser number
    
    def verificarIntegridad(self):
        if isinstance(self.motor, Motor):
            registro= self.motor.registro
            if registro==self.registro:
                if len(self.Asiento)>0:
                    for i in self.asiento:
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
