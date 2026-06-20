def main():

    name = input('Como te llamas? ')
    age = int(input('Que edad tienes? '))
    print(f'Hola, {name}, tienes {age} años')
try:
    main()
except ValueError:
    print('Error: debe introducir un numero entero vaido!')
    main()