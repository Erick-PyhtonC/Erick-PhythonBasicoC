subir=1
def Color(subir):
        ver=input("dime el color que pienso: ")
        if ver=="naranja":
           print("Eres un genio ganaste")
        elif subir<3:
                print("no es ese el color pierdes un intento")
                subir+=1
                Color(subir) 
        else:
            print("pierdes byebye")                    
Color(subir)
