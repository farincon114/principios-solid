import abc


#4 Interface Segretation Principle INCORRECTO


class Metodos_pago(abc.ABC):
    abc.abstractclassmethod
    def Pago(self,order,Sms_Confirmacion):
        pass

class CreditoMetodosDePago(Metodos_pago):
    def Pago(self, order, codigo_seguridad,Sms_Confirmacion):
        return super().Pago(order, codigo_seguridad,Sms_Confirmacion)

class DebitoMetodosDePago(Metodos_pago):
    def Pago(self, order, codigo_seguridad,Sms_Confirmacion):
        return super().Pago(order, codigo_seguridad,Sms_Confirmacion)

class PseMetodosdePago(Metodos_pago):
    def Pago(self, order, Email_addres,Sms_Confirmacion):
        return super().Pago(order, Email_addres,Sms_Confirmacion)

''' En este ejemplo estamos defiendo un metodo de confirmacion
de SMS de pago a todas class de metodos de pago, pero en realidad
la unica que lo va nesecitar el el pago por PSE ya que los demas
tienen un codigo de seguridad en el cual puede pasar el pago
estariamos faltando al principio de segregacion de interfaces, 
la mejor forma de crearlo seria el siguiente ejemplo'''



#4 Interface Segretation Principle CORRECTO

class Metodos_pago(abc.ABC):
    abc.abstractclassmethod
    def Pago(self,order):
        pass
    def Confirmacion(self,Sms_Confirmacion):
        pass

class CreditoMetodosDePago(Metodos_pago):
    def Pago(self, order, codigo_seguridad):
        return super().Pago(order, codigo_seguridad)

class DebitoMetodosDePago(Metodos_pago):
    def Pago(self, order, codigo_seguridad):
        return super().Pago(order, codigo_seguridad)

class PseMetodosdePago(Metodos_pago):
    def Pago(self, order, Email_addres):
        return super().Pago(order, Email_addres)
    def Confirmacion(self,Sms_Confirmacion):
        self.Sms_Confirmacion = Sms_Confirmacion

''' creamos una interfaz que va tener como opcion la confirmacion
de pago por el sms pero solo al que realmente
lo va a  nesecitar,  sin obligar a los demas metodos a usarla 
asi cumplimos con el principio '''       
    
