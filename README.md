
# Simulador básico de App de viagens urbanas

Pequeno projeto em Python que simula um aplicativo de viagens
(imagens, documentos, planilhas, vídeos, compactados, outros).

## Recursos utilizados:
- Python 3
- `os` para limpar a tela 
- `random` para simular o "aceite" dos motoristas
- `time` para obter a hora atual (simular horario normal/pico)

## Conceitos praticados neste projeto

- Uso de funçoes para reutilização do código.
- Listas para cadastrar os locais usados como origem e destino
- Uso de dicionários para mapear as distancias
- Uso do Time para obter hora atual
- Simulação do horarios com random para simular horarios normal e de pico.


## Motivação

Criar um simuilador de app de viagens para treinar lógica de programação, manipulação de dados, loops e validação de entrada de dados.


## Como o programa funciona

1. O usuário informa o local de origem e o destino.
2. O programa:
   - valida se os locais estao cadastrados.
   - calcula a distancia e o valor da corrida
   - solicita confirmação da viagem ao usuário:	
     se 'Sim' inicia a busca de um motorista e inicia a viagem
     se 'Não' agradece ao usuário e finaliza o programa		
   
## Estrutura das funções principais

- `limpa_tela()`: limpa a yela apos cada interação com o usuário.
- `bem_vindo()`: Exibe o nome da empresa e uma mensagem de bem vindo.
- `busca_motorista(hora_atual, horarios_pico, km)`: recebe os parametros usados para verificar o horário e a km
   e simula uma busca e aceite de um motorista parceiro
- `simula_viagem(km)`: simula a viagem mostrando a km percorrida e a km total (ex: km 1/15)
   e informa quando a viagem for concluida
- `finaliza()`: limpa a tela, exibe uma mensagem de agradecimento e encerra o programa

##  Como executar

1. Clone o repositório ou baixe os arquivos.
2. Instale o Python 3, se ainda não tiver.
3. No terminal, dentro da pasta do projeto, execute: python app_corrida_v2.py

## Avaliação do ChatGPT:

✅ Pontos positivos do código

✔ Boa separação em funções

✔ Simulação de tempo bem feita

✔ Uso correto de listas e dicionários

✔ Interface amigável

✔ Código legível e organizado


<br>📌 Resumo dos principais erros críticos corrigidos.
   
✔ Uso de `km` como variável global

✔ Função finaliza() duplicado

✔ Hora aleatória limitada

✔ Falta de limite no loop<br>


<br>🚀 Avaliação: Perfeito 😄

Está ótimo como aprendizado — você praticou funções, listas, 
dicionários, loops, validação de entrada, lógica condicional
e até simulação de tempo. Isso já é muito conteúdo bem aplicado.

Contatos:

[![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:wanderrbrito@gmail.com)


[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wanderlei-rbrito/)


[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wanderrbrito/)
