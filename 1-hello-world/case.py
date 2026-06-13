number = 1

match number:
    case 1:
        print("Seleccionaste la opcion 1")
    case 2:
        print("Seleccionaste la opcion 2")
    case 3:
        print("Seleccionaste la opcion 3")
    case _:
        print('Opcion no valida!')

def option(number):
    response = None
    if number == 1:
        response = 'Seleccionaste la opcion 1'
        #return 'Selecciionaste la opcion 1'
    elif number == 2:
        response = 'Seleccionaste la opcion 2'
        #return 'Selecciionaste la opcion 2'
    elif number == 3:
        response = 'Seleccionaste la opcion 3'
        #return 'Selecciionaste la opcion 3'
    else:
        response = 'Opcion no valida!'
        #return 'Opcion no valida!'
    return response

result = option(9)
print(result)