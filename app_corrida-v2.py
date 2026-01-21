#!/usr/bin/env python3
"""
Programa: App_corrida
Descrição: Simulador básico de App de viagens urbanas
Versao: 2.0
Autor: Wanderlei Rocha Brito
Correcao: ChatGPT disponivel no Readme.md   
Data: 21/01/2026
"""
import os
import random
import time
import datetime

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def bem_vindo():
    print('==== 🚗 Bem vindo ao Bora-lá 🚗 ====')
    print('== Seu App genérico de viagem ==\n')

def busca_motorista(hora_atual, horarios_pico, km):
    inicio = time.time()
    motorista_encontrado = False

    while not motorista_encontrado:
        time.sleep(1)
        limpa_tela()
        bem_vindo()
        tempo_decorrido = int(time.time() - inicio)

        # Limite de espera
        if tempo_decorrido > 120:
            print("❌ Nenhum motorista disponível no momento.")
            finaliza()
            #return

        if hora_atual not in horarios_pico:
            aceite = random.randint(1, 50)
            if aceite != 31:
                print(f'[{tempo_decorrido}s] Buscando 🚗 parceiro ...')
            else:
                print(f'✅ Motorista encontrado após {tempo_decorrido} segundos!\n')
                motorista_encontrado = True
        else:
            aceite = random.randint(1, 100)
            if aceite != 57:
                print(f'\033[31m##⚠ Alta demanda ##\033[0m Buscando 🚗 parceiro ...')
            else:
                print(f'✅ Motorista encontrado após {tempo_decorrido} segundos!\n')
                motorista_encontrado = True

    time.sleep(1)
    print('🚗 Motorista aguardando no local de embarque')
    time.sleep(2)
    simula_viagem(km)

def simula_viagem(km):
    limpa_tela()
    bem_vindo()
    print("\n🚗 Iniciando viagem...\n")

    for i in range(1, int(km) + 1):
        time.sleep(0.5)
        print(f"🚗 {i}/{km} km percorridos")

    print("\n✅ Viagem concluída! Você chegou ao destino.")
    finaliza()

def finaliza():
    time.sleep(1)
    limpa_tela()
    print('🙏 Obrigado por escolher o Bora-lá!')
    time.sleep(2)
    exit()

# Lista de locais
locais = [
    'Casa', 'Oficina', 'Centro', 'Henrique', 'Mineirao',
    'Shopping', 'Aeroporto', 'Rodoviaria', 'Uesb', 'Hospital'
]

# Distâncias
distancias = {
    'Casa': [0, 8.5, 6, 6, 4, 5, 15, 6, 6, 5],
    'Oficina': [8.5, 0, 3, 9, 7, 6, 13, 8, 9, 6],
    'Centro': [6, 4, 0, 7, 8, 8, 21, 8.9, 6, 10],
    'Henrique': [5, 9, 6, 0, 8, 9, 20, 11, 5, 11],
    'Mineirao': [4, 9, 6, 5, 0, 4, 15, 5, 6, 5],
    'Shopping': [4, 9, 6, 5, 3, 0, 15, 5, 6, 5],
    'Aeroporto': [15, 9, 6, 5, 3, 4, 0, 5, 6, 5],
    'Rodoviaria': [5, 9, 8.9, 5, 3, 4, 15, 0, 6, 5],
    'Uesb': [6, 8, 6, 5, 3, 4, 15, 5, 0, 5],
    'Hospital': [5, 8.5, 6, 5, 3, 4, 15, 5, 6, 0]
}

# Hora atual (simulada)
hora_atual = random.randint(0, 23)
print(f'Hora atual: {hora_atual}')

# Horários de pico
horarios_pico = [8, 9, 12, 13, 17, 18, 21]

# Valores
vlr_normal = 2.21
vlr_pico = vlr_normal * 1.3


while True:
    limpa_tela()
    bem_vindo()

    origem = input('Informe sua origem: ').strip().title()
    destino = input('Informe seu destino: ').strip().title()

    if origem in locais and destino in locais and origem != destino:
        indice = locais.index(destino)
        km = distancias[origem][indice]

        print(f'\n📍 Distância de {origem} até {destino}: {km} km')

        if hora_atual not in horarios_pico:
            valor = km * vlr_normal
            print(f'💰 Valor da corrida: R$ {valor:.2f}')
        else:
            valor = km * vlr_pico
            print(f'\033[31m⚠ Alta demanda\033[0m | 💰 Valor: R$ {valor:.2f}')

        aceita = input('\nConfirma a corrida (S/N): ').upper()

        if aceita == 'S':
            busca_motorista(hora_atual, horarios_pico, km)
        else:
            print('❌ Viagem cancelada.')
            finaliza()
    else:
        print('❌ Dados inválidos.')
        opcao = input('Deseja tentar novamente? (S/N): ').upper()
        if opcao != 'S':
            finaliza()
            break
