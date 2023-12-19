class Descuento:
    def __init__(self):
        self._porcentaje = 1

    @property
    def porcentaje(self):
        return self._porcentaje

    @porcentaje.setter
    def porcentaje(self, valor):
        self._porcentaje = valor


class DescuentoEstudiante(Descuento):
    def __init__(self):
        super().__init__()
        self.porcentaje = 0.7


class DescuentoInvierno(Descuento):
    def __init__(self):
        super().__init__()
        self.porcentaje = 0.9


class Cliente:
    def __init__(self):
        self.precio_base = 1000
        self.descuentos = []

    def agregar_descuento(self, descuento):
        self.descuentos.append(descuento)

    def calcular_precio(self):
        pass


class Turista(Cliente):
    def calcular_precio(self):
        return self.precio_base * sum(descuento.porcentaje for descuento in self.descuentos)


class Business(Cliente):
    def calcular_precio(self):
        return (self.precio_base * 1.5) * sum(descuento.porcentaje for descuento in self.descuentos)


class Premium(Business):
    def __init__(self):
        super().__init__()
        self.recargo = 200

    def calcular_precio(self):
        precio_con_descuentos = super().calcular_precio()
        return precio_con_descuentos + self.recargo


class Pasaje:
    def __init__(self, cliente):
        self.cliente = cliente

    def precio(self):
        return self.cliente.calcular_precio()


# Ejemplo de uso
descuento_estudiante = DescuentoEstudiante()
descuento_invierno = DescuentoInvierno()

cliente_turista = Turista()
cliente_turista.agregar_descuento(descuento_estudiante)

cliente_business = Business()
cliente_business.agregar_descuento(descuento_estudiante)

cliente_premium = Premium()
cliente_premium.agregar_descuento(descuento_estudiante)
cliente_premium.agregar_descuento(descuento_invierno)

pasaje_turista = Pasaje(cliente_turista)
pasaje_business = Pasaje(cliente_business)
pasaje_premium = Pasaje(cliente_premium)

print(pasaje_turista.precio())  # Precio con descuento estudiante
print(pasaje_business.precio())  # Precio con descuento estudiante y recargo
print(pasaje_premium.precio())  # Precio con descuento estudiante y descuento invierno y recargo
