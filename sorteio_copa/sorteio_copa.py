import os
import random

os.system('cls')
random.seed(42)

grupos = {}
selecoes = [
    'Austrália', 'RI6', 'RI4', 'Arábia Saudita', 'Catar', 'Coreia do Sul', 'Irã', 'Japão',
    'RI3', 'Jordânia', 'Uzbequistão', 'África do Sul', 'Argélia', 'Cabo Verde', 'Costa do Marfim',
    'Egito', 'Gana', 'Marrocos', 'Senegal', 'Tunísia', 'Colômbia', 'Equador', 'Paraguai', 'RI1',
    'Uruguai', 'Nova Zelândia', 'Áustria', 'Croácia', 'RI5', 'Escócia', 'RI2', 'Noruega', 'Suíça',
    'Curaçau', 'Haiti', 'Panamá'
]
cabecas = [
    'México', 'Canadá', 'Estados Unidos', 'Brasil', 'Espanha', 'Argentina',
    'França', 'Inglaterra', 'Portugal', 'Holanda', 'Bélgica', 'Alemanha'
]
letra = [
    'Grupo_A', 'Grupo_B', 'Grupo_C', 'Grupo_D', 'Grupo_E', 'Grupo_F',
    'Grupo_G','Grupo_H','Grupo_I','Grupo_J','Grupo_K','Grupo_L'
]

# Inicializa todos os grupos como listas vazias
for i in range(12):
    grupos[letra[i]] = []

# Define manualmente alguns cabeças de chave
grupos['Grupo_A'].append('México')
grupos['Grupo_B'].append('Canadá')
grupos['Grupo_D'].append('Estados Unidos')

# Remove os já fixados da lista de cabeças
cabecas.remove('México')
cabecas.remove('Canadá')
cabecas.remove('Estados Unidos')

# Sorteia os demais cabeças para os grupos restantes
for i in range(12):
    list_name = letra[i]
    if list_name in ['Grupo_A', 'Grupo_B', 'Grupo_D']:
        continue
    sorteio = random.choice(cabecas)
    grupos[list_name].append(sorteio)
    cabecas.remove(sorteio)

# Distribui as seleções nos grupos
while selecoes:
    for s in range(12):
        if not selecoes:  # evita erro quando lista esvaziar
            break
        list_name = letra[s]
        sorteio_selecoes = random.choice(selecoes)
        grupos[list_name].append(sorteio_selecoes)
        selecoes.remove(sorteio_selecoes)

# Exibe resultado
print('====== SORTEIO DAS SELEÇÕES ====')
print('=== COPA DO MUNDO FIFA 2026 ===')
print(60 * '=')
for name, my_list in grupos.items():
    print(f"{name}: {my_list}")
    print(60 * '*')