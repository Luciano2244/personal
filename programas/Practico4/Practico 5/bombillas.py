class Bombilla:
    def __init__(self):
        self.__estado=False
    @property
    def estado(self):
        return self.__estado
    def encender(self):
        self.__estado=True
    def apagar(self):
        self.__estado=False
if __name__=="__main__":
    mi_bombilla=Bombilla()
    otra_bombilla=Bombilla()
    mi_bombilla.encender()
    print(mi_bombilla.estado)    