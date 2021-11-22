# tienda de ropa online

#2. Principio abierto-cerrado INCORRECTO

from _typeshed import Self
from typing import ClassVar


class Descuento:            
    # identificas cliente y precio del articulo             
    def __init__(self,cliente,precio):
        self.cliente = cliente
        self.precio = precio

    # asignas el tipo de descuento para cada cliente con condicionales abiertas 
    def tipo_cliente(self):                   
        if self.cliente == 'basico':
            return self.precio * 0.2
        if self.cliente == 'medio':
            return self.precio * 0.4
        if self.cliente == 'vip':
            return self.precio *0.6
        else:
            print('a un no eres cliente preferencia :(')

""" esta mal por que estamos modificando el valor de la funcion del descuento todo
el tiempo, recuerden que, debe estar abierta para su extencion , pero cerrada
para su modificacion, en este caso debemos extender la funcion pero cerrado para su
modificacion 
"""

#2. Principio abierto-cerrado CORRECTO

class Descuento:            
    # identificas cliente y precio del articulo             
    def __init__(self,cliente,precio):
        self.cliente = cliente
        self.precio = precio
    # defines cliente y valor del descuento
    def basico_descuento(self): 
        return self.precio * 0.2

    # extiendes el descuento mas no modificas el cerrado.
class Medio_cliente(Descuento):
    def basico_descuento(self):
        return super().basico_descuento() * 2

    # nuevamente extiendes el descuento mas no modificas el cerrado.
class Vip_cliente(Medio_cliente):
    def basico_descuento(self):
        return super().basico_descuento() * 2

"""como pudimos observar en este codigo por medio de clases
 extendimos las funciones (descuento), pero no modificamos ninguna cerrada  """
        
        
