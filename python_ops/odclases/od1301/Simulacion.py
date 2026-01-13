from model.gestion_bancaria import CuentaBancaria
from model.Cliente import Cliente
"""Creacion de todas las cuentas"""
ban1 = CuentaBancaria(1000, 'ban1')
ban2 = CuentaBancaria(2000, 'ban2')
ban3 = CuentaBancaria(3000, 'ban3')
ban4 = CuentaBancaria(4000, 'ban4')
ban5 = CuentaBancaria(5000, 'ban5')
ban6 = CuentaBancaria(6000, 'ban6')
ban7 = CuentaBancaria(7000, 'ban7')
ban8 = CuentaBancaria(8000, 'ban8')
ban9 = CuentaBancaria(9000, 'ban9')
ban10 = CuentaBancaria(10000, 'ban10')

"""Creacion de todos los clientes"""
c1 = Cliente("Cliente1", [ban1, ban2])
c2 = Cliente("Cliente2", [ban3, ban4])
c3 = Cliente("Cliente3", [ban5, ban6])
c4 = Cliente("Cliente4", [ban7, ban8])
c5 = Cliente("Cliente5", [ban9, ban10])

"""Simulacion"""
ban1.depositar(100)
ban2.retirar(100)
c1.mostrar_info()
ban1.retirar(200)
ban1.mostrar_movimientos()
print(f"\n{c1}")
