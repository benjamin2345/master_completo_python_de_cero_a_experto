def sayHello(name):
    print("Este script se ejecuta solo si el script es ejecutado de forma directa!")
    print(f"Hola {name}")

# Este bloque sirve para comprobar si estás ejecutando el archivo .py directamente o si solo lo estás importando desde otro archivo.
# Si ejecutas el script directamente, Python establece la variable __name__ en "__main__". Si lo importas en otro programa,
# toma el nombre del archivo.

# Si ejecutas este archivo directamente, esto se imprimirá.
# Si lo importas desde otro archivo, esta parte no se ejecutará.
if __name__ == '__main__': #este se ejecuta cuando el codigo se ejecuta directamente
    print("Hi, World")
    sayHello('Benja')
