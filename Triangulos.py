#Autor: Samara Andrea Vega
#Leer el valor de cada uno de los lados de un triángulo, posteriormente indica el tipo de triángulo, según sus características



def clasificarTriangulo(ladoA, ladoB, ladoC):
    if (ladoA==ladoB==ladoC):
        return "Equilátero"
    else:
        if (ladoA==ladoB or ladoA==ladoC or ladoB==ladoC):
            return "Isósceles"
        else:
            return "Otro"



def main():
    
    ladoUno = int(input("Teclea el valor del primer lado del triángulo: "))
    ladoDos = int(input("Teclea el valor del segundo lado del triángulo: "))
    ladoTres = int(input("Teclea el valor del tercer lado del triángulo: "))

    tipoDeT = clasificarTriangulo(ladoUno, ladoDos, ladoTres)
    
    if (ladoUno+ladoDos)>ladoTres and (ladoUno+ladoTres)>ladoDos and (ladoDos+ladoTres)>ladoUno:
        print("Tipo de triángulo: ", tipoDeT)
    else:
        print("Estos lados no corresponden a un triángulo")
    


main()
