def main():
    name = input('introduce el nombre del producto: ')
    #print(name)

    price = int(input('introduce el precio del producto en dolares: '))
    #print(f'El valor final {price} pesos:')

    weight = float(input('Ingresa el peso en gramos: '))
    #print(f'Pesa {weight} gramos.')
    print(f'Producto: {name}\nPrecio: {price} USD \nPeso: {weight}')


try:
    main()

except ValueError:
    print('Error: debes introducir bien los datos, decimal es con punto!')
    main()