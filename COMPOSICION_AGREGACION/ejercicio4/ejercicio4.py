class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"Ropa(tipo='{self.tipo}', material='{self.material}')"


class Ropero:
    def __init__(self, material):
        self.material = material
        self.ropas = [None] * 20
        self.nroRopas = 0

    def agregar_ropa(self, ropa):
        if self.nroRopas < 20:
            self.ropas[self.nroRopas] = ropa
            self.nroRopas += 1
            return True
        return False

    def eliminar_por_material(self, mat):
        i = 0
        while i < self.nroRopas:
            if self.ropas[i].material.lower() == mat.lower():
                self.ropas[i] = self.ropas[self.nroRopas - 1]
                self.nroRopas -= 1
            else:
                i += 1

    def eliminar_por_tipo(self, tipo):
        i = 0
        while i < self.nroRopas:
            if self.ropas[i].tipo.lower() == tipo.lower():
                self.ropas[i] = self.ropas[self.nroRopas - 1]
                self.nroRopas -= 1
            else:
                i += 1

    def mostrar_por_material(self, mat):
        print(f"\nPrendas de material {mat}:")
        for i in range(self.nroRopas):
            if self.ropas[i].material.lower() == mat.lower():
                print("  -", self.ropas[i])

    def mostrar_por_tipo(self, tipo):
        print(f"\nPrendas de tipo {tipo}:")
        for i in range(self.nroRopas):
            if self.ropas[i].tipo.lower() == tipo.lower():
                print("  -", self.ropas[i])

    def mostrar(self):
        print("\nContenido del ropero:")
        for i in range(self.nroRopas):
            print("  -", self.ropas[i])


# main

if __name__ == "__main__":

    ropero = Ropero("Madera")
    ropero.agregar_ropa(Ropa("Camisa", "Algodón"))
    ropero.agregar_ropa(Ropa("Pantalón", "Jean"))
    ropero.agregar_ropa(Ropa("Chaqueta", "Cuero"))
    ropero.agregar_ropa(Ropa("Remera", "Algodón"))
    ropero.agregar_ropa(Ropa("Pollera", "Seda"))
    ropero.mostrar()
    ropero.mostrar_por_material("Algodón")
    ropero.mostrar_por_tipo("Chaqueta")
    print("\nEliminando prendas de algodón...")
    ropero.eliminar_por_material("Algodón")
    ropero.mostrar()
    print("\nEliminando prendas tipo Jean...")
    ropero.eliminar_por_tipo("Jean")
    ropero.mostrar()
