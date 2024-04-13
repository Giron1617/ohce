## se crean las funciones para procesar las solicitudes de saludo y palindromo


## funcion salu = la funcion retorna la respuesta dependiendo de la hora atraves de los if's.
def salu(nom,h):
    if h >= 20 or h < 6:
        return "buenas noches {}" .format(nom)
    elif h >=6 and h < 12:
        return "buenos dias {}" .format(nom)
    else:
        return "buenas tardes {}" .format(nom)
    
