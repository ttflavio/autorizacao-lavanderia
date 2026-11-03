
def verificar_autorizacao(saldo, preco):

    # Validar o saldo
    if type(saldo) is not int or saldo < 0:
        return {
            "resultado": "Entrada inválida",
            "saldo_final": None,
            "mensagem": "O saldo deve ser um inteiro maior ou igual a zero."
        }

    # Validar o preço
    if type(preco) is not int or preco <= 0:
        return {
            "resultado": "Entrada inválida",
            "saldo_final": saldo,
            "mensagem": "O preço deve ser um inteiro maior que zero."
        }

    # Verificar se existe saldo suficiente
    if saldo >= preco:
        return {
            "resultado": "Autorizado",
            "saldo_final": saldo - preco,
            "mensagem": "Serviço autorizado com sucesso."
        }

    return {
        "resultado": "Recusado",
        "saldo_final": saldo,
        "mensagem": "Saldo insuficiente."
    }

def iniciar_programa():
    preco = 15

    print("=== Sistema de Autorização ===")

    try:
        saldo = int(input("Digite a quantidade de créditos: "))
    except ValueError:
        print("Entrada inválida: digite um número inteiro.")
        return

    resultado = verificar_autorizacao(saldo, preco)

    print("\n=== Resultado ===")
    print("Status:", resultado["resultado"])
    print("Saldo final:", resultado["saldo_final"])
    print("Mensagem:", resultado["mensagem"])


if __name__ == "__main__":
    iniciar_programa()

