try:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado = num1 / num2  # ZeroDivisionError: division by zero
except ValueError:
    print("Debe ingresar un valor numérico.")
except ZeroDivisionError:
    print("Debe ingresar un valor distinto de cero en el denominador.")
except:
    print("Ha ocurrido un error.")
else:
    try:
        print(resultado)
    except:
        print("Ha ocurrido un error.")
finally:
    print("Esta línea siempre se ejecuta.")

print("Fin del programa.")
