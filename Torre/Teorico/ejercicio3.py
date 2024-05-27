"""Se desea llevar un control del estado de una cuenta corriente; la cuenta corriente
está caracterizada por su saldo y sobre ella se pueden realizar tres tipos de
operaciones:
a. saldo: devuelve el saldo de la cuenta (puede ser negativo).
b. imposición (cantidad): ingresa en la cuenta una cantidad de dinero.
c. reintegro (cantidad): saca de la cuenta una determinada cantidad de dinero.
Suponga que la cuenta inicialmente tiene un saldo de cero.
d. Escriba una clase CuentaCorriente que implemente la funcionalidad descrita;
escriba otro método para probar su funcionamiento"""
from decimal import Decimal
class CuentaCorriente():
    def __init__(self, cantidad):
        self.cantidad=cantidad
    def saldo(self):
        return self.cantidad
    def imposicion(self):
        num=input("ingrese= ")
        self.cantidad+=float(num)
        return self.cantidad 
    def reintegro (self):
        num=input("ingrese= ")
        self.cantidad-=float(num)
        return self.cantidad
if __name__ == "__main__":
    money=CuentaCorriente(0)
    money.imposicion()
    money.reintegro()
    print(money.saldo())
