from dispositivo import Dispositivo

class Database:
    def __init__(self, diccionario):
        self.database = []
        for dispositivo in diccionario['dispositivos']:
            self.database.append(Dispositivo(diccionario = dispositivo))
        

    def delete_by_id(self, id):
        for dispositivo in self.database:
            if dispositivo.id == id:
                self.database.remove(dispositivo)
        
    def add_dispositivo(self, dispositivo = None, diccionario = {}):
        if diccionario == {}:
            self.database.append(dispositivo)
        else:    
            self.database.append(Dispositivo(diccionario = diccionario))
        
if __name__ == '__main__':
    pass