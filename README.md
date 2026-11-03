# Sistema de Autorização por Saldo

## 1. Sobre o projeto

Este projeto foi desenvolvido em Python para simular a autorização de um serviço com base no saldo disponível de um cliente.

O sistema recebe o saldo e o preço do serviço, valida os dados e informa se a operação foi autorizada, recusada ou se os dados são inválidos.

## 2. Regras de negócio

- O saldo e o preço devem ser números inteiros.
- O saldo deve ser maior ou igual a zero.
- O preço deve ser maior que zero.
- A autorização acontece quando o saldo é maior ou igual ao preço.
- Quando autorizado, o valor do serviço é descontado do saldo.
- Quando recusado, o saldo permanece inalterado.
- Entradas inválidas não podem autorizar nem realizar descontos.

## 3. Estrutura do projeto

- `main.py`: contém a função responsável pela validação e autorização.
- `testes.py`: executa os testes e compara os resultados observados com os esperados.

## 4. Como executar

É necessário ter Python instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python testes.py
```

O programa apresentará os resultados dos testes, indicando se cada um passou ou falhou.

## 5. Testes realizados

| Saldo | Preço | Resultado esperado | Saldo final esperado |
|---:|---:|---|---:|
| 30 | 15 | Autorizado | 15 |
| 10 | 15 | Recusado | 10 |
| 15 | 15 | Autorizado | 0 |
| 5 | 8 | Recusado | 5 |
| -1 | 3 | Entrada inválida | Indisponível |
| 30 | 0 | Entrada inválida | 30 |

**Resultado:** 6 de 6 testes aprovados.

## 6. Tecnologias utilizadas

- Python
- Visual Studio Code
- Git e GitHub (para controle de versão e compartilhamento do projeto)