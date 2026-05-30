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
