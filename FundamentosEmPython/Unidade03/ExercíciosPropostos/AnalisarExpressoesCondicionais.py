# Defina as variáveis x = 10, y = 20, z = 30
# Execute a expressão condicional:
# (x < y and y > z) or (x + y == z and not (z == x * 3))
# Determine se a expressão retorna True ou False

x, y, z = 10, 20, 30

expressaoCondicional = (x < y and y > z ) or (x + y == z and not(z == x * 3)) # falso ou falso
print(expressaoCondicional) # falso