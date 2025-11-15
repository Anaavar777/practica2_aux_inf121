class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.participantes = []

    def agregar_participante(self, participante):
        self.participantes.append(participante)


class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.participantes = []

    def agregar_participante(self, participante):
        # Validar que no esté en otra fraternidad
        if participante.fraternidad is not None:
            raise ValueError(f"{participante.nombre} ya pertenece a una fraternidad.")
        self.participantes.append(participante)
        participante.fraternidad = self


class Participante:
    def __init__(self, nombre, edad, facultad):
        self.nombre = nombre
        self.edad = edad
        self.facultad = facultad
        self.fraternidad = None

        facultad.agregar_participante(self)

    def __str__(self):
        fr = self.fraternidad.nombre if self.fraternidad else "Ninguna"
        return f"{self.nombre} - Edad: {self.edad} - Facultad: {self.facultad.nombre} - Fraternidad: {fr}"
# main
if __name__ == "__main__":
    fac_ing = Facultad("Ingeniería")
    fac_edu = Facultad("Educación")
    p1 = Participante("Luis", 20, fac_ing)
    p2 = Participante("María", 19, fac_ing)
    p3 = Participante("Carlos", 22, fac_edu)
    p4 = Participante("Ana", 18, fac_edu)
    p5 = Participante("Jorge", 21, fac_ing)
    frat_sicuris = Fraternidad("Sicuris del Alba", encargado="Profesor Ramos")
    frat_caporales = Fraternidad("Caporales Fuego", encargado="Señora Pérez")

    frat_sicuris.agregar_participante(p1)
    frat_sicuris.agregar_participante(p3)

    frat_caporales.agregar_participante(p2)
    frat_caporales.agregar_participante(p4)

    fac_ing = Facultad("Ingeniería")
    fac_edu = Facultad("Educación")

    p1 = Participante("Luis", 20, fac_ing)
    p2 = Participante("María", 19, fac_ing)
    p3 = Participante("Carlos", 22, fac_edu)
    p4 = Participante("Ana", 18, fac_edu)
    p5 = Participante("Jorge", 21, fac_ing)

    frat_sicuris = Fraternidad("Sicuris del Alba", encargado="Profesor Ramos")
    frat_caporales = Fraternidad("Caporales Fuego", encargado="Señora Pérez")

    frat_sicuris.agregar_participante(p1)
    frat_sicuris.agregar_participante(p3)

    frat_caporales.agregar_participante(p2)
    frat_caporales.agregar_participante(p4)

    print("=== Lista de Participantes ===")
    for p in [p1, p2, p3, p4, p5]:
        print(p)
    print("\n=== Encargados de Fraternidades ===")
    print(f"{frat_sicuris.nombre} → Encargado: {frat_sicuris.encargado}")
    print(f"{frat_caporales.nombre} → Encargado: {frat_caporales.encargado}")
    print("\n=== Edades de Participantes ===")
    for p in [p1, p2, p3, p4, p5]:
        print(f"{p.nombre}: {p.edad} años")
    try:
        frat_sicuris.agregar_participante(p2) 
    except ValueError as e:
        print("\nError detectado correctamente:", e)
