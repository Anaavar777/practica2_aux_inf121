class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def info(self):
        return f"{self.nombre} - {self.puesto} - salario: {self.salario}"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empresa(self):
        print("Empresa:", self.nombre)
        for e in self.empleados:
            print(e.info())

    def buscar_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                return e
        return None

    def eliminar_empleado(self, nombre):
        self.empleados = [e for e in self.empleados if e.nombre.lower() != nombre.lower()]

    def salario_promedio(self):
        if not self.empleados:
            return 0
        total = sum(e.salario for e in self.empleados)
        return total / len(self.empleados)

    def empleados_con_salario_mayor(self, valor):
        return [e for e in self.empleados if e.salario > valor]


e1 = Empleado("Ana", "Gerente", 5000)
e2 = Empleado("Luis", "Programador", 3500)
e3 = Empleado("Carla", "Diseñadora", 3200)
e4 = Empleado("Jorge", "Programador", 4000)

empresa = Empresa("TechCorp")
empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)
empresa.agregar_empleado(e3)
empresa.agregar_empleado(e4)

empresa.mostrar_empresa()

print("Buscar empleado:", empresa.buscar_empleado("Luis").info())

empresa.eliminar_empleado("Carla")
print("Después de eliminar a Carla:")
empresa.mostrar_empresa()

print("Salario promedio:", empresa.salario_promedio())

print("Empleados con salario mayor a 3600:")
lista = empresa.empleados_con_salario_mayor(3600)
for e in lista:
    print(e.info())
