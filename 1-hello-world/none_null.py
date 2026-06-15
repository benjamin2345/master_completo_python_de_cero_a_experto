

text = 'hola'
if text:
    print('Pasa por que el texto no esta vacio ')

text = ''
if text:
    print('pasa? o no pasa?')

text = ' '
if text:
    print('pasa? o no pasa?')

text = ' '.strip() #elimina un espacio vacio
if text:
    print('pasa el texto? o no pasa?')

personas = ['pepe', 'maria']
if personas:
    print('pasa por que tiene elementos en la lista')

personas = []
if personas:
    print('pasa por que tiene elementos en la lista')

number = 0
if number:
    print('pasa el numero?')

number = 1
if number:
    print('pasa el numero?')

personas = None
if personas is not None:
    print('perfecto la lista contiene elementos')

if text is not None:
    print('el texto no es None o null')
elif text:
    print('el texto no es vacio')
else:
    print('el texto es vacio')

