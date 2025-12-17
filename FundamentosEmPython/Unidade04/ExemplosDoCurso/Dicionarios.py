# Definindo um dicionario de estados de máquinas industriais
estados_maquinas = {
    "maquina_1": "oeracional",
    "maquina_2": "manutencao",
    "maquina_3": "parada",
    "maquina_4": "operacional"
}

# Acessando o estado de uma máquina especifica
print(f"O estado da máquina 1 é:", estados_maquinas["maquina_1"])

# Modificando o estado de uma máquina
estados_maquinas["maquina_2"] = "operacional"
print(f"Os estados atualizados das máquinas são: {estados_maquinas}")