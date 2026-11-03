from main import verificar_autorizacao

testes = [
    (30, 15, "Autorizado", 15),
    (10, 15, "Recusado", 10),
    (15, 15, "Autorizado", 0),
    (5, 8, "Recusado", 5),
    (-1, 3, "Entrada inválida", None),
    (30, 0, "Entrada inválida", 30)
]

for saldo, preco, resultado_esperado, saldo_esperado in testes:

    observado = verificar_autorizacao(saldo, preco)

    passou = (
        observado["resultado"] == resultado_esperado
        and observado["saldo_final"] == saldo_esperado
    )

    print(f"Saldo: {saldo} | Preço: {preco}")
    print(f"Esperado: {resultado_esperado} | Saldo final: {saldo_esperado}")
    print(f"Observado: {observado}")
    print("Teste:", "PASSOU" if passou else "FALHOU")
    print("-" * 40)