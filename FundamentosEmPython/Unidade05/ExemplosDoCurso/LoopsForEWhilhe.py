# Exemplo de for
for i in range(10):
    print("Produto", i + 1, "verificado.")

# Exemplo de for com listas
ordem = ["segunda", "terça", "quarta", "quinta", "sexta"]

for x in ordem:
    print("Dia da semana:", x)

# Exemplo de while
# Temperatura inicial em graus Celsius
temperatura = 20

# Enquanto a temperatura for menor ou igual a 25
while temperatura <= 25:
    print(f"Temperatura atual: {temperatura:.2f}°C")
    temperatura += 1 # Aumenta a temperatura em 1 grau °C

# Loop while: Monitoramento contínuo

# Importando a biblioteca necessária para simular o tempo
import time

# Definindo o consumo de energia inicial
consumo_energia = 50  # Consumo inicial em kW
limite_superior = 100  # Limite superior de consumo seguro em kW

# Laço de repetição para monitorar o consumo de energia
while True:  
    print(f"Consumo de energia atual: {consumo_energia} kW")  
    if consumo_energia > limite_superior:
        print("Alerta: Consumo de energia acima do limite seguro!")
        break  # Sai do loop se o limite for ultrapassado

    # Simulando a variação do consumo de energia
    consumo_energia += 10  # Aumenta o consumo em 10 kW
    time.sleep(2)  # Pausa de 2 segundos entre as leituras

print("Monitoramento encerrado.")

# Loop for: Iterando com range(), lista e dicionário

# O loop irá iterar de 1 a 5, representando cada ciclo de consumo
for ciclo in range(1, 6):
    # Cálculo do consumo de energia para o ciclo atual
    consumo = 50 + (ciclo * 8)
    # Exibe o ciclo e o respectivo consumo de energia em kW
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo} kW")

# Usando for e listas

# Lista com dados simulados de consumo de energia
leituras = [55, 63, 70, 95, 105]  

# Itera sobre cada leitura na lista
for leitura in leituras:
    # Verifica se a leitura de consumo excede o limite de 100 kW
    if leitura > 100:
        print(f"Alerta! Consumo de {leitura} kW excedeu o limite!")
    else:
        print(f"Consumo dentro do limite: {leitura} kW")

# Usando for com dicionário

# Dicionário contendo o consumo de energia em diferentes setores
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

# Itera sobre cada setor e seu respectivo consumo de energia
for setor, consumo in consumo_setores.items():
    # Determina o status do consumo com base no limite de 100 kW
    if consumo > 100:
      status = "acima do limite" 
    else:
      status = "dentro do limite"
    # Exibe o setor, o consumo e o status
    print(f"Setor: {setor} | Consumo: {consumo} kW – Status: {status}")