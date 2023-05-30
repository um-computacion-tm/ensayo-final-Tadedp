class Dispositivo:
    def __init__(self, id = 0, nombre = '', marca = '', tipo = '', diccionario = {}):
        if diccionario != {}:
            self.id = diccionario.get('id', 0)
            self.nombre = diccionario.get('nombre', '')
            self.tipo = diccionario.get('tipo', '') 
            self.marca = diccionario.get('marca', '')
        else:
            self.id = id
            self.nombre = nombre
            self.tipo = tipo
            self.marca = marca                

if __name__ == '__main__':
    pass