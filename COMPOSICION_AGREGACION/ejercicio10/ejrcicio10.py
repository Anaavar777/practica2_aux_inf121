class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci


class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad


class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket


class Charla:
    def __init__(self, lugar, nombreCharla, speaker, participantes=None):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.speaker = speaker
        self.participantes = participantes if participantes else []

    @property
    def np(self):
        return len(self.participantes)


class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.charlas = []

    def agregar_charla(self, charla):
        self.charlas.append(charla)

    def edad_promedio(self):
        edades = []
        for charla in self.charlas:
            for p in charla.participantes:
                edades.append(p.edad)
        return sum(edades) / len(edades) if edades else 0

    def buscar_persona(self, nombre, apellido):
        for charla in self.charlas:
            if charla.speaker.nombre == nombre and charla.speaker.apellido == apellido:
                return True
            for p in charla.participantes:
                if p.nombre == nombre and p.apellido == apellido:
                    return True
        return False

    def eliminar_charlas_por_speaker(self, ci):
        self.charlas = [c for c in self.charlas if c.speaker.ci != ci]

    def ordenar_charlas_por_participantes(self):
        self.charlas.sort(key=lambda c: c.np, reverse=True)


sp1 = Speaker("Ana", "Gómez", 34, 111, "IA")
sp2 = Speaker("Luis", "Pérez", 40, 222, "Ciberseguridad")
sp3 = Speaker("Carla", "Mendoza", 29, 333, "Robótica")

p1 = Participante("Mario", "López", 22, 444, 10)
p2 = Participante("Sara", "Rivas", 28, 555, 11)
p3 = Participante("Jorge", "Lima", 31, 666, 12)
p4 = Participante("Elena", "Suárez", 20, 777, 13)

c1 = Charla("Auditorio A", "Introducción a IA", sp1, [p1, p2])
c2 = Charla("Sala 2", "Ataques Modernos", sp2, [p3])
c3 = Charla("Sala 3", "Robots Sociales", sp3, [p1, p3, p4])

evento = Evento("TechWeek")
evento.agregar_charla(c1)
evento.agregar_charla(c2)
evento.agregar_charla(c3)

print("a) Edad promedio:", evento.edad_promedio())
print("b) Buscar 'Mario López':", evento.buscar_persona("Mario", "López"))
print("   Buscar 'Pedro Torres':", evento.buscar_persona("Pedro", "Torres"))
evento.eliminar_charlas_por_speaker(222)
print("Charlas restantes tras eliminación:")
for ch in evento.charlas:
    print(ch.nombreCharla)
evento.ordenar_charlas_por_participantes()
print("Charlas ordenadas por participantes:")
for ch in evento.charlas:
    print(ch.nombreCharla, "-", ch.np, "participantes")
