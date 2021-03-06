# tienda de ropa online
from _typeshed import Self
import abc


#3 Liskov Substitution Principle INCORRECTO

class Metodos_pago(abc.ABC):      #creamos una clase abstracta para metodos de pago./define la orden de pago y codigo de seguridad para las tarjetas
    abc.abstractclassmethod
    def Pago(self,order,codigo_seguridad):
        pass

class CreditoMetodosDePago(Metodos_pago):    # creamos una herencia de metodos de pago/asignamos la def a pago con t. credito
    def Pago(self, order, codigo_seguridad):
        return super().Pago(order, codigo_seguridad)

class DebitoMetodosDePago(Metodos_pago):      # creamos una herencia de metodos de pago/asignamos la def a pago con t. debito
    def Pago(self, order, codigo_seguridad):
        return super().Pago(order, codigo_seguridad)


class PseMetodosdePago(Metodos_pago):      # creamos una herencia de metodos de pago/asignamos la def a pago con pse
    def Pago(self, order, codigo_seguridad):
        return super().Pago(order, codigo_seguridad)


'''se crea un metodo con  orden de pago y un codigo de seguridad para las opciones
 de pago pero encontramos que el pago pse no funciona con codigo de seguirdad si no
con correo electronico estamos faltando al principio de sustitucion de liskov'''



#3 Liskov Substitution Principle CORRECTO


class Metodos_pago(abc.ABC):   #creamos una clase abstracta para metodos de pago./define la orden de pago
    abc.abstractclassmethod
    def Pago(self,order):
        pass

class CreditoMetodosDePago(Metodos_pago):                 # creamos una herencia de metodos de pago/asignamos la def a pago con t. credito
    def  __init__(self,codigo_seguridad):                 #esta def, asigna los datos de seguidad para la tarjeta
        self.codigo_seguridad = codigo_seguridad
        
    def Pago(self, order,):                               #esta def, asigna la orden de pago
        return super().Pago(order)


class DebitoMetodosDePago(Metodos_pago):                 # creamos una herencia de metodos de pago/asignamos la def a pago con pse
    def  __init__(self,codigo_seguridad):                #esta def, asigna los datos de seguidad para la tarjeta
        self.codigo_seguridad = codigo_seguridad         

    def Pago(self, order):                               #esta def, asigna la orden de pago
        return super().Pago(order)


class PseMetodosdePago(Metodos_pago):
    def  __init__(self,correo_electronico):
        self.correo_electronico = correo_electronico
        
    def Pago(self, order, correo_electronico):
        return super().Pago(order, correo_electronico)


''' ahora lo que se realizo fue crear una orden de pago en la superclase
y en cada subclase se creo un metodo para definir como se pagara la orden de pago '''
