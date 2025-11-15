class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        if doctor not in self.doctores:
            self.doctores.append(doctor)

    def mostrar_doctores(self):
        print("Hospital:", self.nombre)
        for d in self.doctores:
            print(d.nombre, "-", d.especialidad)


d1 = Doctor("Ana Gómez", "Cardiología")
d2 = Doctor("Luis Pérez", "Pediatría")
d3 = Doctor("Carla Mendoza", "Traumatología")

h1 = Hospital("Hospital Central")
h2 = Hospital("Clínica Vida")

h1.agregar_doctor(d1)
h1.agregar_doctor(d2)
h2.agregar_doctor(d1)
h2.agregar_doctor(d3)

h1.mostrar_doctores()
h2.mostrar_doctores()
