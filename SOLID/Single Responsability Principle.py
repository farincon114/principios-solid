# tienda de ropa online

# 1. Principio de responsabilidad única CORRECTO

class Cliente:

    def __initial__(self,nombre: str, apellido: str):               #se crea una clase para solicitar los datos del cliente 
        self.nombre = nombre
        self.apellido = apellido


class metodos_pago:

    def tarjetas_credito(self,numero:int, fecha:int/int, cvc:int):                 #se crea otra clase para asignar los metodos de pago del cliente
            self.numero = numero
            self.fecha = fecha
            self.cvc = cvc
            
    def tarjetas_debito(self):
            pass    
        
        
        

# 1. Principio de responsabilidad única INCORRECTO


class Cliente:

    def __initial__(self,nombre: str, apellido: str):               #se esta asignando una responsabilidad de solicitar los datos del cliente
        self.nombre = nombre
        self.apellido = apellido

    def tarjetas_credito(self,numero:int, fecha:int/int, cvc:int):      #se esta asignando otra responsabilidad en la misma clase asignar los metodos de pago del cliente
            self.numero = numer
            self.fecha = fecha
            self.cvc = cvc
            
    def tarjetas_debito(self):
            pass   

  
    


