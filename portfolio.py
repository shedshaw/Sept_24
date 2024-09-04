
def spc():
  print("~" * 20)    

class calculadora:  
     def __init__(self):
         pass
     def listaC(self):
         opcionesCalc= ["1.Suma", "2.Resta", "3.Multiplicación", "4.División",]
         print("\n".join(opcionesCalc))
     def suma(self, a , b):
         return a + b
     def resta(self, a , b):
         return a - b
     def multiplicacion(self, a , b):
         return a * b
     def division(self, a , b):
         if a == 0 or b == 0:
             print("No se puede dividir por 0")
             if a == 0:
                 a = input("Vuelva a ingresar el primer dígito: ")
             elif b == 0:
                 b = input("Vuelva a ingresar el segundo dígito: ")
         else:
             return a / b

def main():
  def saludo():
      print("Bienvenido al portafolio de septiembre de 2024")
  def opciones1():
    opciones= ["1. Calculadora", "2.", "3.", "4.", "5.",]
    print("Elija una de las siguientes opciones: ")
    print("\n".join(opciones))
    opcion = int(input("Ingrese el número de la opción que desea: "))
    if opcion == 1:
      operacion = "si"
      total = "si"
      calc = calculadora()
      calc.listaC()
      opc = int(input("Ingrese la operación que desea realizar: "))
      if opc == 1:
          operacion = "suma"
          num1 = int(input("Ingrese el primer dígito: "))
          num2 = int(input("Ingrese el segundo dígito: "))
          total = calc.suma(num1, num2)
          resultado = f"El resultado de la {operacion} es {total}"
          print(resultado)
  
      elif opc == 2:
            operacion = "resta"
            num1 = int(input("Ingrese el primer dígito: "))
            num2 = int(input("Ingrese el segundo dígito: "))
            total = calc.resta(num1, num2)
            resultado = f"El resultado de la {operacion} es {total}"
            print(resultado)
          
      elif opc == 3:
            operacion = "multiplicacion"
            num1 = int(input("Ingrese el primer dígito: "))
            num2 = int(input("Ingrese el segundo dígito: "))
            total = calc.multiplicacion(num1, num2)
            resultado = f"El resultado de la {operacion} es {total}"
            print(resultado)
      elif opc == 4:
            operacion = "division"
            num1 = int(input("Ingrese el primer dígito: "))
            num2 = int(input("Ingrese el segundo dígito: "))
            if num1 == 0 or num2 == 0:
                print("No se puede dividir por 0")
                if num1 == 0:
                    num1 = input("Vuelva a ingresar el primer dígito: ")
                elif num2 == 0:
                    num2 = input("Vuelva a ingresar el segundo dígito: ")
            else:
              pass
            total = calc.division(num1, num2)
            resultado = f"El resultado de la {operacion} es {total}"
            print(resultado)
      else:
            print("Opción inválida")
  
  
  saludo()
  opciones1()

main()
