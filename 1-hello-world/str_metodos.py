name = 'Benjamin Avila'
course = 'Curso de python'
name_upper = name.upper()

#print(name.upper())
print(name == name_upper)
print(name_upper)
print(name)
print(course.lower())

words = 'curso de python'
print(words.capitalize()) #solo la primera letra de la cadena la hace mayuscula
print(words.title()) #cada letra se convierte mayuscula

words = '     hola Benjamin     '
print(words.strip()) # esta instruccion elimina todos los espacios de la cadena
print(words.lstrip()) # esta instruccion elimina los espacios de la izquierda
print(words.rstrip()) # esta instruccion elimina todos los espacios de la derecha

text = 'Hola Java'
new_text = text.replace('Java','Python')
print(text)
print(new_text)

text = 'Benjamin,Avila,Python,Java,Angular'
data_list = text.split(',')
print(data_list)
print(data_list[2])
print(data_list[4])

data = ['Benjamin', 'Avila', 'Python', 'Java', 'Angular']
text = '/'.join(data)
print(text)

text = 'Hola, Benjamin que tal como estas?'
print(text.find('Benjamin'))
print(text.find('Benjamín')) # marca -1 cuando no lo encuentra
print(text.find('tal'))
print(text.index('como'))
#print(text.index('coma')) #marca error cuando no lo encuentra

print(text.startswith('Benjamin')) #regresa un booleano
print(text.startswith('hola'))
print(text.startswith('Hola,'))
print(text.endswith('?'))

number = '1234'
decimal = '1234.45'
text = 'Python'
mix = 'Python2'

print(number.isnumeric())
print(number.isdigit())
print(decimal.isdecimal())
print(text.isalnum())
print(mix.isalpha())
print(text.isalpha())

text = '    hola Benjamin como estas, bienvenido al curso de Python!     '
text_clean = text.strip().capitalize()
print(text_clean)
text_clean = text.strip().capitalize().title()
print(text_clean)

new_text = text_clean.replace('Curso De Python', 'Curso de Python 3')
print(new_text)

words = new_text.split()
print(words)
