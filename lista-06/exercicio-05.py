# 5. Classificação de Times de Futebol
# Crie uma tupla contendo os 10 primeiros colocados de um campeonato de
# futebol. Depois, exiba:
# • Os três primeiros colocados.
# • Os últimos três colocados.
# • Os times em ordem alfabética.
# • A posição de um time específico informado pelo usuário.

times = ("Palmeiras", "Santos", "Grêmio", "Internacional", "Flamengo", "Fluminense", "Botafogo", "Vasco", "Bahia", "São Paulo")

print("Os três primeiros colocados são:")
for time in times[:3]:
    print(time)

print("\nOs três últimos colocados são:")
for time in times[-3:]:
    print(time)

print("\nOs times em ordem alfabética são:")
for time in sorted(times):
    print(time)

time_escolhido = input("Digite o nome de um time: ")
posicao_time_escolhido = times.index(time_escolhido) if time_escolhido in times else -1

if posicao_time_escolhido != -1:
    print(f"A posição do time {time_escolhido} é {posicao_time_escolhido + 1}.")
else:
    print(f"O time {time_escolhido} não está na lista.")