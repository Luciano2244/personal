import os
class Bombilla:
    def __init__(self,estado):
        self.est=estado
    def Cambiar(self,nuevo_estado):
        self.est=nuevo_estado
    def obtener_info(self):
        return self.est
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__=="__main__":
    bom=Bombilla("off")
    while True:
        choice = input("Press enter to continue or type [exit]\n")
        clear_terminal()
        if choice.lower()=="exit":
            print("Exiting...")
            break  
        elif choice.lower()=="":
            if bom=="on"or"off":
                print('Turn on or off?:')
                bom=Bombilla(input())
                print('The bulb is:')
                print(bom.obtener_info())
            elif bom!="on"or"off":
                print('error')
                break
        else:
            print('error')
            break
    