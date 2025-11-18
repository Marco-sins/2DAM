from abc import ABC, abstractmethod

class Empleado:
    """La clase original de empleado"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @abstractmethod
    def calcular_salario(self):
        """Prototipo de la funcion que van a implementar los hijos"""
        pass

class EmpleadoTiempoCompleto(Empleado):
    """Empleado que cobra un sueldo fijo y hereda de la clase empleado"""
    def __init__(self, name, id, salario):
        super().__init__(name, id)
        self.salario = salario
    
    def calcular_salario(self):
        print(f"{self.name} ID: ({self.id}) - Salario: {self.salario}")

class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas y hereda de la clase empleado"""
    def __init__(self, name, id, horas, salario):
        super().__init__(name, id)
        self.horas = horas
        self.salario = salario

    def calcular_salario(self):
        print(f"{self.name} ID: ({self.id}) - Salario: {self.salario * self.horas}")

class EmpleadoComision(Empleado):
    """La clase de empleado que cobra por comision y hereda de la clase empleado"""
    def __init__(self, name, id, salario, comision):
        super().__init__(name, id)
        self.salario = salario
        self.comision = comision

    def calcular_salario(self):
        print(f"{self.name} ID: ({self.id}) - Salario: {self.salario + self.comision}")


def mostrar_salarios(empleados):
    """Esto muestra los salarios de todos los empleados"""
    for empleado in empleados:
        empleado.calcular_salario()
    

empleados = [
    EmpleadoTiempoCompleto("Ana", 1, 3000),
    EmpleadoPorHoras("Luis", 2, 20, 160),
    EmpleadoComision("Marta", 3, 1500, 500)
]

mostrar_salarios(empleados)
