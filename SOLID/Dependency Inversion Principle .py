
from abc import ABC,abstractmethod


# clase de autorizacion por sms
class AutorizacionSMS:
    def __init__(self):
        self.autorizacion = False

    def codigo_verificacion(self, code):
        print(f"verificando su  codigo de SMS {code}")
        self.autorizacion = True

    def is_authorized(self) -> bool:
        return self.autorizacion


# clase para poder realizar procesos de pago
class Procesos_pago(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class CreditoProcesos_pago(Procesos_pago):
    pass

class PseProcesos_pago(Procesos_pago):
    pass


'''en este ejemplo creamos un funcion para autorizacion de pago, pero que ocurre si en la autorizacion
solo la tenemos con sms, y queremos agregar mas formas, nos tocaria modificar todo el codigo
ya que dependemos un clase estariamos faltando al principio en ese caso seria mejor realizarlo como 
el otro ejemplo.
'''


# clase  para autorizacion
class Autorizacion(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

# clase abstraida de la autorizacion
class AuthorAutorizacionSMSizer_SMS(Autorizacion):

    def __init__(self):
        self.autorizacion = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.autorizacion = True

    def is_authorized(self) -> bool:
        return self.autorizacion

# clase abstraida de la autorizacion
class Google_Autorizacion(Autorizacion):

    def __init__(self):
        self.autorizacion = False

    def verify_code(self, code):
        print(f"Verifying Google auth code {code}")
        self.autorizacion = True

    def is_authorized(self) -> bool:
        return self.autorizacion

# clase abstraida de la autorizacion
class Robot_Autorizacion(Autorizacion):

    def __init__(self):
        self.autorizacion = False

    def not_a_robot(self):
        self.autorizacion = True

    def is_authorized(self) -> bool:
        return self.autorizacion

class Procesos_pago(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class CreditoProcesos_pago(Procesos_pago):
    pass

class PseProcesos_pago(Procesos_pago):
    pass

'''en este caso realizamos creamos una abstraccion de autorizacion para que se pueda
realizar por medio de metodos abstractos mas no que dependan.'''