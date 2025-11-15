class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Medicamento(Producto):
    def __init__(self, nombre, precio, principio_activo, requiere_receta):
        super().__init__(nombre, precio)
        self.principio_activo = principio_activo
        self.requiere_receta = requiere_receta


class Cosmetico(Producto):
    def __init__(self, nombre, precio, tipo_piel, marca):
        super().__init__(nombre, precio)
        self.tipo_piel = tipo_piel
        self.marca = marca


class Lote:
    def __init__(self, codigo_lote, fecha_fabricacion):
        self.codigo_lote = codigo_lote
        self.fecha_fabricacion = fecha_fabricacion
        self.registros = []  

    def agregar_registro(self, registro):
        self.registros.append(registro)


class Registro:
    def __init__(self, fecha, cantidad):
        self.fecha = fecha
        self.cantidad = cantidad

# main
if __name__ == "__main__":
    med1 = Medicamento("Paracetamol", 5.0, "Paracetamol", True)
    cos1 = Cosmetico("Crema Hidratante", 15.0, "Seca", "MarcaX")

    lote1 = Lote("L001", "2024-01-15")
    registro1 = Registro("2024-02-01", 100)
    registro2 = Registro("2024-03-01", 150)

    lote1.agregar_registro(registro1)
    lote1.agregar_registro(registro2)

    print(f"Medicamento: {med1.nombre}, Precio: ${med1.precio}, Principio Activo: {med1.principio_activo}, Requiere Receta: {med1.requiere_receta}")
    print(f"Cosmético: {cos1.nombre}, Precio: ${cos1.precio}, Tipo de Piel: {cos1.tipo_piel}, Marca: {cos1.marca}")
    print(f"Lote Código: {lote1.codigo_lote}, Fecha de Fabricación: {lote1.fecha_fabricacion}")
    for reg in lote1.registros:
        print(f"  Registro - Fecha: {reg.fecha}, Cantidad: {reg.cantidad}")
