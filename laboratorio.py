class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_info(self):
        return [self.nombre, self.precio]

class Medicamento(Producto):
    def __init__(self, nombre, precio, compuesto, porcentaje):
        super().__init__(nombre, precio)
        self.compuesto = compuesto
        self.porcentaje = porcentaje
    def get_info(self):
        return [self.nombre, self.precio, self.compuesto, self.porcentaje]

class Lab():
    def __init__(self, nombre, lista_productos):
        self.nombre = nombre
        self.lista_productos = lista_productos
    def info_laboratorio(self):
        lista_info_lab = []
        for i in range(len(lista_productos)):
            lista_info_lab.append(lista_productos[i].get_info())
        return lista_info_lab

producto_1 = Producto("Crema solar", 4)
producto_2 = Medicamento("Ibuprofeno", 5, "lactosa", 0.5)
producto_3 = Producto("Cepillos de dientes", 3)
lista_productos = []
lista_productos.append(producto_1)
lista_productos.append(producto_2)
lista_productos.append(producto_3)
laboratorio1 = Lab("Medialab", lista_productos)
print("El laboratorio tiene", laboratorio1.info_laboratorio())
