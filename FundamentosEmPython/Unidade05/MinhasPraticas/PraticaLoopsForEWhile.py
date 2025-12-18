# Exemplo de for
for i in range(10):
    print("Produto", i + 1, "verificado.")

# Exemplo de for com listas
ordem = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

for x in ordem:
    print("Dia da semana:", x)

# Exemplo de while
# Temperatura inicial em graus Celsius
temperatura = 12

# Enquanto a temperatura for menor ou igual a 25
while temperatura <= 50:
    print(f"Temperatura atual: {temperatura:.2f}°C")
    temperatura += 1 # Aumenta a temperatura em 1 grau °C


import time

# Definindo o consumo de energia inicial
consumo_energia = 50  # Consumo inicial em kW
limite_superior = 100  # Limite superior de consumo seguro em kW

# Laço de repetição para monitorar o consumo de energia
while True:  
    print(f"Consumo de energia atual: {consumo_energia} kW")  
    if consumo_energia > limite_superior:
        print("Alerta: Consumo de energia acima do limite seguro!")
        break  

    # Simulando a variação do consumo de energia
    consumo_energia += 20  # Aumenta o consumo em 10 kW
    time.sleep(5)  

print("Monitoramento encerrado.")

for ciclo in range(1, 4):
   
    consumo = 50 + (ciclo * 8)
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo} kW")

# Lista com dados simulados de consumo de energia
leituras = [80, 75, 95, 105]  

# Itera sobre cada leitura na lista
for leitura in leituras:
    # Verifica se a leitura de consumo excede o limite de 100 kW
    if leitura > 100:
        print(f"Alerta! Consumo de {leitura} kW excedeu o limite!")
    else:
        print(f"Consumo dentro do limite: {leitura} kW")

# Dicionário contendo o consumo de energia em diferentes setores
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

for setor, consumo in consumo_setores.items():
    if consumo > 120:
      status = "acima do limite" 
    else:
      status = "dentro do limite"
    # Exibe o setor, o consumo e o status
    print(f"Setor: {setor} | Consumo: {consumo} kW – Status: {status}")