from model.gestion_bancaria import CuentaBancaria

class Cliente:
    def __init__(self, nombre, cuenta_bancaria):
        """
        Docstring for __init__: Inicializa el objeto
        
        :param self: Apunta al propio objeto
        :param nombre: Nombre del cliente
        :param cuenta_bancaria: Lista de cuentas bancarias del cliente
        """
        self._nombre = nombre
        self._cuenta_bancaria = cuenta_bancaria

    def agregar_cuenta(self, cuenta_bancaria):
        """
        Docstring for agregar_cuenta: Agrega una cuenta a la lista
        
        :param self: Apunta al propio objeto
        :param cuenta_bancaria: Nueva cuenta a añadir a la lista
        """
        self._cuenta_bancaria.append(cuenta_bancaria)

    def mostrar_info(self):
        """
        Docstring for mostrar_info: Muestra la informacion del cliente
        
        :param self: Apunta al propio objeto
        """
        print(f"Cliente: {self._nombre}")
        for cuenta in self._cuenta_bancaria:
            cuenta.mostrar_saldo()

    def _mostrar_cuentas(self):
        """
        Docstring for _mostrar_cuentas: Muestra todas las cuentas de un cliente
        
        :param self: Apunta al propio objeto
        """
        txt = ""
        i = 0
        for cuenta in self._cuenta_bancaria:
            if i != 0:
                txt += ', '
            txt += f'({cuenta})'
            i += 1
        return txt

    
    def __str__(self):
        return f"Nombre: {self._nombre}, Cuentas: {self._mostrar_cuentas()}"