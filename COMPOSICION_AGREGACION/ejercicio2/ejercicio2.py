class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.nombre} - {self.cargo} - ${self.sueldo}"


class Departamento:
    def __init__(self, nombre, area, empleados=None):
        self.nombre = nombre
        self.area = area
        self.empleados = empleados if empleados else []

    def mostrarEmpleados(self):
        print(f"\nDepartamento: {self.nombre} ({self.area})")
        if not self.empleados:
            print("   No tiene empleados.")
        else:
            for emp in self.empleados:
                print("  -", emp)

    def cambioSalario(self, nuevo_salario):
        for emp in self.empleados:
            emp.sueldo = nuevo_salario

    def contieneEmpleado(self, empleado):
        return empleado in self.empleados

    def moverEmpleadosA(self, otro_departamento):
        otro_departamento.empleados.extend(self.empleados)
        self.empleados.clear()
        
#main

if __name__ == "__main__":
    emp1 = Empleado("Ana", "Ingeniera", 50000)
    emp2 = Empleado("Luis", "Analista", 45000)
    emp3 = Empleado("Marta", "Gerente", 70000)

    depto1 = Departamento("Desarrollo", "Tecnología", [emp1, emp2])
    depto2 = Departamento("Ventas", "Comercial")

    depto1.mostrarEmpleados()
    depto2.mostrarEmpleados()

    print("\nCambiando salario de empleados en Desarrollo a $55000...")
    depto1.cambioSalario(55000)
    depto1.mostrarEmpleados()

    print("\n¿Contiene Luis en Desarrollo?", depto1.contieneEmpleado(emp2))
    print("¿Contiene Marta en Desarrollo?", depto1.contieneEmpleado(emp3))

    print("\nMoviendo empleados de Desarrollo a Ventas...")
    depto1.moverEmpleadosA(depto2)
    depto1.mostrarEmpleados()
    depto2.mostrarEmpleados()