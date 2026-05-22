#age: int = 40 # esta forma es explicita, el compilador detecta que es entero
age = 40
name = 'Benjamin' # es str

print(name + ' tiene ' + str(age) + ' anios') # tienes que convertirlo en string el int

number_str = '30'
number = int(number_str)
print(50 - int(number_str))
print(50 + int(number_str))
print(50 * int(number_str))
print(50 / int(number_str))

x = 10
print(x)
x = 'hola que tal'
print(x)
