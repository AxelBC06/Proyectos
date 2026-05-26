import random
class banco:
    
    def __init__(self):
        self.saldo= 10000
        self.contador = 0
        self.contador2 = 0
        self.contador3 = 0
        self.lista = []
        self.lista2=[]

    def mostrar(self):
     print (f"El credito disponible es de:{self.saldo}$")
     self.contador2 = self.contador2 + 1

    def depositar(self):
       deposito=int(input("Cuanto dinero va a depositar?: "))
       if deposito > 20000:
          print ("para esta cantidad de dinero necesita ir a nuestra sucursal!")
       elif deposito<= 20000:   
        self.saldo = self.saldo + deposito
        print(f"Su total ahora es de:{self.saldo}$")
        self.contador = self.contador + 1
        self.lista.append(f"Deposito por: {deposito}$")
        

    def retirar(self):
       retiro=int(input("Cuanto dinero deseas retirar?: "))
       if retiro > self.saldo:
          print("no tiene suficiente dinero")
       else:  
         self.saldo = self.saldo - retiro
         self.contador3 = self.contador3 + 1
         self.lista2.append(f"retiro por: {retiro}$")
         print(f"Ud a retirado {retiro}$ su total ahora es de:{self.saldo}$")
         a=0
         b=0
         c=0
         while retiro !=0:
            if retiro >= 100:
               retiro = retiro - 100
               a = a + 1 
            elif retiro >= 50:
               retiro -= 50
               b += 1
            else:
               retiro -=1
               c += 1
       
       print (f"ud a recibido {a} billetes de 100$, {b} billetes de 50$,{c} billetes de 1$")
    def historial(self):
       for i in self.lista:
          print(i)
       print (f"ud a realizado un total de {self.contador} depositos ")
       for e in self.lista2:
          print(e)   
       print (f"ud a realizado un total de {self.contador3} retiros")
       print (f"ud a consultado {self.contador2} su saldo")
       
    def salir(self):
       despedida = ["Adios, gracias por utilizar el programa!", "Hasta luego, gracias por utilizar el programa","Nos vemos, gracias por utilizar el programa","los vidrios, gracias por utilizar el programa homie!","se cuida pa, gracias por utilizar el programa"]
       despedida_aleatoria = random.choice(despedida)
       print(despedida_aleatoria)
      

def saludar():
    saludos = ["klk", "Buenos días","sup!","¡bienvenido!","Qué tal"]
    
    saludo_aleatorio = random.choice(saludos)
    print(saludo_aleatorio)


cajero = banco()

menu = 0
saludar()
while menu != 5:
    menu = int(input("(((((menu))))) \n 1-Mostrar Saldo \n 2-Depositar  \n 3-Retirar \n 4-Historial \n 5-Salir\nDigite su opcion :"))
    if menu == 1:
       cajero.mostrar()     
    if menu ==2:
       cajero.depositar()   
    if menu==3:
       cajero.retirar()    
    if menu== 4 :
     cajero.historial()   
    if menu == 5:
     cajero.salir()           
    

    

        