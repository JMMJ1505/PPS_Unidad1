lista_inicial = [6,14,11,3,2,1,15,19]

numero_introducido = int(input("Introduce un numero entre el 1 y 20: "))
    
def numero_correcto(numero_a_comprobar):
        if numero_a_comprobar > 20 or numero_a_comprobar < 1 :
            print("El numero introduce se sale del rango solicitado")
        else:
            estaEnLista(numero_a_comprobar, lista_inicial)


def estaEnLista(valor, lista):
    for numero in lista:
        if numero == valor:
            esta_en_lista = True
        else:
            esta_en_lista = False
    if esta_en_lista == True:
        print("Su numero se encuentra en la lista")
    else: 
        print("Su numero no se encuentra en la lista")
    
    
numero_correcto(numero_introducido)