import os

os.system('cls' if os.name =='nt' else 'clear')

competidores = {}

qtde = int(input('Informe a quantidade de participantes da competição: '))

for i in range(qtde):
    nome = input(f"Nome do {i+1}º participante: ")
    notas = []
 
    for n in range(5):
        nota = float(input(f'Digite a {n+1}ª nota do competidor {nome} (Valor: 0/10): '))    
        notas.append(nota)

    maior = max(notas)
    menor = min(notas)

    notas.remove(maior)
    notas.remove(menor)

    media_final = sum(notas) / len(notas)

    competidores[nome] = {
        "notas": notas,
        "media": round(media_final, 2)
    }

comp_ordenado = dict(sorted(competidores.items(), key=lambda item: item[0][1]))

print("\nResultado da competição excluindo a maior e menor nota!!:")

for participante, dados in comp_ordenado.items():
    print(f"{participante} → notas válidas: {dados['notas']} | média: {dados['media']}")


maior_media = max(dados["media"] for dados in competidores.values())

vencedores = [
    nome for nome, dados in competidores.items()
    if dados["media"] == maior_media
]

print("\n🏆 RESULTADO FINAL 🏆")

if len(vencedores) == 1:
    print(f"Vencedor: {vencedores[0]} com média {maior_media}")
else:
    print(f"Empate! Vencedores com média {maior_media}:")
    for nome in vencedores:
        print(f"- {nome}")
