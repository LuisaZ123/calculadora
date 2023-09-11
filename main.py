class calculadora():
    
    def suma (self,a,b):
        return a+b
    
    def resta (self,a,b):
        return a-b
    
    def multiplicación (self,a,b):
        return a*b
    
    def división (self,a,b):
        return a//b
    
    def potenciación (self, a,b):
        return a**b
    
calculadora = calculadora

print ("Seleccone la operación que desea realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Potenciación ")

Respuesta = input()

a= input("Escriba el valor de a: ")
b= input("Escriba el valor de b: ")

Respuesta = int(Respuesta)
if Respuesta == 1:
    print("La suma es: ", calculadora.suma(a, b))

if Respuesta == 2:
    print("La resta es: ", calculadora.resta(a,b))

if Respuesta == 3:
    print("El producto es: ", calculadora.multiplicación(a,b))

if Respuesta == 4:
    print("La división es: ", calculadora.división(a,b))

if Respuesta == 5:
    print("la potencia es: ", calculadora.potenciación(a,b))
    