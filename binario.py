def esBinario(strbinario):
    try:
        num_binario= set(strbinario)  
        comprobar_binario = {"0", "1"} 
        if comprobar_binario == num_binario or num_binario == {'1'} or num_binario == {'0'}:
            num_a_decimal = int(strbinario, 2)
            print("Su numero es binario y en decimal es: ", num_a_decimal)
        else:
            print("Introduzca un numero correcto")
    except TypeError:
        return print("ERROR")

esBinario("1001")    
        
            
        
    

     
        
    