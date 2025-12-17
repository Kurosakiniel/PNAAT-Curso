# Criação e inicialização de uma lista
temperaturas_celsius = [25.1, 25.5, 24.9, 26.0, 25.8]
print(f"Leituras iniciais de temperatura: {temperaturas_celsius}")

# Adicionando novas leituras á lista
temperaturas_celsius.append(26.2)
temperaturas_celsius.append(25.7)
print(f"Leituras após novas coletas: {temperaturas_celsius}")

# Acessando elementos específicos
temperaturas_celsius.append(26.2)
temperaturas_celsius.append(25.7)
print(f"Leituras após novas coletas: {temperaturas_celsius}")

# Modificando uma leitura
temperaturas_celsius[2] = 25.0  # Supondo que a terceira leitura (índice 2) foi corrigida
print(f"Leituras após correção: {temperaturas_celsius}")

# Removendo uma leitura
temperaturas_celsius.pop(0)  # Remove o primeiro elemento (leitura mais antiga)
print(f"Leituras após remover a mais antiga: {temperaturas_celsius}")

# Verificando o tamanho da lista
print(f"Número total de leituras registradas: {len(temperaturas_celsius)}")

# Verificando a existência de um valor
if 26.2 in temperaturas_celsius:
    print("A temperatura de 26.2°C foi registrada.")

# Ordenando as leituras
temperaturas_celsius.sort()
print(f"Leituras ordenadas: {temperaturas_celsius}")