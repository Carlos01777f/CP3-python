temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_maior_risco = 0
maior_criticos = -1

for i in range(len(temperaturas)):
    sala = temperaturas[i]
    numero_sala = i + 1

    media = sum(sala) / len(sala)

    criticos = 0
    for temp in sala:
        if temp >= 33:
            criticos += 1

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {criticos}")
    print()

    if criticos > maior_criticos:
        maior_criticos = criticos
        sala_maior_risco = numero_sala

print(f"Sala com maior risco: Sala {sala_maior_risco}")