
# Simulação de leitura de nível de líquido
nivel_litros =  10 
nivel_maximo = 30
nivel_minimo = 12

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
pressao_atual = 6.5  
pressao_maxima = 5.0  
pressao_minima = 1.1

print(f'Pressão atual: {pressao_atual} bar')

# Lógica condicional para controle da pressão
if pressao_atual > pressao_maxima and pressao_atual > 4.0:
    print("Atenção: Pressão crítica! Acionando alívio de pressão.")
elif pressao_atual < pressao_minima or pressao_atual < 2.0:
    print("Atenção: Pressão muito baixa! Acionando compressor.")
else:
    print("Pressão dentro dos limites normais.")
