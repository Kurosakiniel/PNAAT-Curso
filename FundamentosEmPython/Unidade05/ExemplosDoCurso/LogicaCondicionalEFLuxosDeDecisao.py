# Exemplo 01: Controle de Nível de Líquido

# Simulação de leitura de nível de líquido
nivel_litros = 50  # Nível atual do líquido em litros
nivel_maximo = 100  # Nível máximo permitido em litros
nivel_minimo = 20  # Nível mínimo seguro em litros

print(f'Nível atual do líquido: {nivel_litros} litros')

# Lógica condicional para controle do nível de líquido
if nivel_litros > nivel_maximo:
    print("Atenção: Nível do líquido acima do máximo! Acionando sistema de drenagem.")
elif nivel_litros < nivel_minimo:
    print("Atenção: Nível do líquido abaixo do mínimo! Acionando sistema de abastecimento.")
else:
    print("Nível do líquido dentro dos limites normais.")

# Exemplo 02: Monitoramento de Pressão

# Simulação de leitura de pressão
pressao_atual = 3.5  # Pressão atual em bar
pressao_maxima = 5.0  # Pressão máxima permitida em bar
pressao_minima = 1.0  # Pressão mínima segura em bar

print(f'Pressão atual: {pressao_atual} bar')

# Lógica condicional para controle da pressão
if pressao_atual > pressao_maxima and pressao_atual > 4.0:
    print("Atenção: Pressão crítica! Acionando alívio de pressão.")
elif pressao_atual < pressao_minima or pressao_atual < 2.0:
    print("Atenção: Pressão muito baixa! Acionando compressor.")
else:
    print("Pressão dentro dos limites normais.")
