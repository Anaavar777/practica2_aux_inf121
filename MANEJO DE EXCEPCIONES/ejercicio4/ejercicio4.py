class ProductoNoEncontradoException(Exception):
    pass

class StockInsuficienteException(Exception):
    pass

class ProductoInvalidoException(Exception):
    pass


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Inventario:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, p):
        for prod in self.productos:
            if prod.codigo == p.codigo:
                raise ProductoInvalidoException("El código ya existe")

        if p.precio < 0 or p.stock < 0:
            raise ProductoInvalidoException("Precio o stock no pueden ser negativos")

        self.productos.append(p)

    def buscarProducto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontradoException("Producto no encontrado")

    def venderProducto(self, codigo, cantidad):
        p = self.buscarProducto(codigo)
        if p.stock < cantidad:
            raise StockInsuficienteException("Stock insuficiente")
        p.stock -= cantidad
        return p.stock



inventario = Inventario()

try:
    inventario.agregarProducto(Producto("A1", "Mouse", 50, 20))
    inventario.agregarProducto(Producto("A2", "Teclado", 100, 10))
    inventario.agregarProducto(Producto("A1", "Monitor", 500, 5))  
except Exception as e:
    print("Error:", e)

try:
    inventario.agregarProducto(Producto("A3", "Laptop", -2000, 5))  
except Exception as e:
    print("Error:", e)

try:
    inventario.venderProducto("A2", 3)
    inventario.venderProducto("A2", 20)  
except Exception as e:
    print("Error:", e)

try:
    inventario.buscarProducto("A9")  
except Exception as e:
    print("Error:", e)
