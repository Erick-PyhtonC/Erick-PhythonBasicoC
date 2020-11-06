def Color(subir):
     ver=input("dime el color que pienso: ")
     if ver=="naranja" and subir<3:
        print("Eres un genio ganaste")
     else:
        print("no es ese el color pierdes un intento")
        subir+=1
        Color(subir)
Color()
