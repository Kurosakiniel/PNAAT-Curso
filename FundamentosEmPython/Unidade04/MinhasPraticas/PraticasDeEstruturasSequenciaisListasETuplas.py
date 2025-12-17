# Criando uma lista

leituras_sensor = [22.5, 23.1, 24.5, 19.2, 345.0]
print(leituras_sensor)

leituras_sensor.append(23.0)
leituras_sensor.remove(24.5)
print(leituras_sensor)

# Criando uma tupla
coordenadas_gps = (30.71, - 74.00)
print(coordenadas_gps)
coordenadas_gps = (30.71, - 75.00)
print(coordenadas_gps) # não muda mas tem como atualizar, entretanto, é meio inutil