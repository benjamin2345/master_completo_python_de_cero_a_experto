name = 'Benjamin'
age = 43
text = f'Me llamo {name} y tengo {age} anios'
print(text)

a = 5
b = 3
print(f"La suma de {a} y {b} es {a + b}")

result = f'El precio es {a * b} dolares'
print(result)

price = 50
txt = f'Este producto es muy { 'caro' if price > 50 else 'barato'}'
print(txt)

fruit = 'Manzanas'
txt = f"Me encantan las {fruit.upper()}"
print(txt)

price = 59
text = 'EL precio es {price} dolares'
print(text.format(price = 49))

txt = "Oferta por solo {price:.2f} dolares"
print(txt.format(price = 60))
