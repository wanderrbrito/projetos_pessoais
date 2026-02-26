#!/usr/bin/env python
# coding: utf-8

import random

pilotos = [
	'Max Verstappen #3 Red Bull', 'Isack Hadjar #6 Red Bull', 'Lewis Hamilton #44 Ferrari',
	'Charles Leclerc #16 Ferrari', 'Lando Norris #1 McLaren', 'Oscar Piastri #81 McLaren',
	'George Russell #63 Mercedes', 'Kimi Antonelli #12 Mercedes', 'Fernando Alonso #14 Aston Martin', 
	'Lance Stroll #18 Aston Martin', 'Alex Albon #23 Williams', 'Carlos Sainz #55 Williams',
	'Nico Hülkenberg #27 Audi', 'Gabriel Bortoleto #5 Audi', 'Pierre Gasly #10 Alpine',
	'Franco Colapinto #43 Alpine', 'Esteban Ocon #31 Haas', 'Oliver Bearman #87 Haas', 
	'Liam Lawson #30 Racing Bulls', 'Arvid Lindblad #41 Racing Bulls', 'Sergio Pérez #11 Cadillac',
	'Valtteri Bottas #77 Cadillac'
]

def gerar_tempo():
    minutos = random.randint(1,2)
    segundos = random.randint(0,59)
    milesimos = random.randint(0,999)
    return (f'{minutos:02}:{segundos:02}:{milesimos:03}') 

def simular_treino(lista):
    resultado = [(piloto, gerar_tempo()) for piloto in lista]
    resultado.sort(key=lambda x: x[1])
    return resultado

def exibe_sessao(resultado, nome_treino):
    print(f'Resultado do {nome_treino}')
    if nome_treino == 'Q1':
        for pos, piloto in enumerate(resultado, start=1):
            if pos > 16:
                print(f'\033[31m{pos}º - {piloto[0]} => {piloto[1]}\033[0m')
            else:
                print(f'{pos}º - {piloto[0]} => {piloto[1]}')
    elif nome_treino == 'Q2':
        for pos, piloto in enumerate(resultado, start=1):
            if pos > 10:
                print(f'\033[31m{pos}º - {piloto[0]} => {piloto[1]}\033[0m')
            else:
                print(f'{pos}º - {piloto[0]} => {piloto[1]}')
    else:
        for pos, piloto in enumerate(resultado, start=1):
            print(f'{pos}º - {piloto[0]} => {piloto[1]}')
    return resultado

# Iniciando treino Q1 com 22 pilotos
q1 = exibe_sessao(simular_treino(pilotos), 'Q1')

# Eliminando os 6 últimos (posições 17 a 22)
eliminados_q1 = q1[16:]

# classificados para o Q2
classificados_q1, _ = zip(*q1[:16])

# Iniciando treino Q2 com 16 Pilotos
q2 = exibe_sessao(simular_treino(classificados_q1), 'Q2')

# Eliminando os 6 últimos (posições 10 a 16)
eliminados_q2 = q2[10:]

# classificados para o Q2
classificados_q2, _ = zip(*q2[:10])

# Iniciando treino Q3 com 10 Pilotos
q3 = exibe_sessao(simular_treino(classificados_q2), 'Q3')

# Montando o grid de largada
grid = []
grid.extend(q3)
grid.extend(eliminados_q2)
grid.extend(eliminados_q1)

for pos, piloto in enumerate(grid, start=1):
    print(f'{pos}º - {piloto[0]} => {piloto[1]}')

# Exibindo o pole position
pole = grid[0]
print('\nPole_position:', *pole)