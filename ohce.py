## se crean las funciones para procesar las solicitudes de saludo y palindromo


## funcion salu = la funcion retorna la respuesta dependiendo de la hora atraves de los if's.
def salu(nom,h):
    if h >= 20 or h < 6:
        return "buenas noches {}" .format(nom)
    elif h >=6 and h < 12:
        return "buenos dias {}" .format(nom)
    else:
        return "buenas tardes {}" .format(nom)
    
def pro_p(p):
    ## el operador[::-1] puede invertir la cadena, en este caso 'p'.
    p_i=p[::-1]


    if p == "stop":
         return "adios"
    
    ## sin este elif cualquier palabra saldria con la frase 'bonita palabra'.
    elif p_i == p:
         
         return format(p_i)+ " bonita palabra"
    
    else: return format(p_i)