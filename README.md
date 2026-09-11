# ByteBank

## Integrantes

- Thiago Alves

## Descricao

O ByteBank e um sistema bancario de linha de comando escrito em Python puro, sem
bibliotecas externas. Ele roda no terminal e permite cadastrar varias contas, cada
uma com nome do titular, chave pix, saldo, historico de transacoes e fila de boletos.

O programa foi construido em tres niveis. No nivel 1 existe apenas um saldo e as
operacoes basicas de deposito e saque, com validacao de valor negativo, valor invalido
e saldo insuficiente. No nivel 2 entra a lista de contas: e possivel cadastrar contas
diferentes, acessar uma delas pelo numero e transferir dinheiro entre elas por PIX,
usando a chave pix como identificador do destino. No nivel 3 cada conta ganha um
extrato e uma fila de boletos.

Todo o codigo fica em um unico arquivo `main.py`, organizado em funcoes pequenas: as
funcoes de conta, as operacoes, o extrato, os boletos e os dois menus.

## Funcionalidades

### Nivel 1
- Consultar saldo
- Depositar
- Sacar
- Validacao de valor menor ou igual a zero, valor nao numerico e saldo insuficiente

### Nivel 2
- Cadastrar conta (recusa nome ou chave em branco e chave pix repetida)
- Acessar conta pelo numero
- PIX entre contas (recusa chave inexistente e transferencia para a propria conta)

### Nivel 3
- Extrato com todas as transacoes da conta
- Estorno da ultima transacao
- Agendar boletos
- Ver a fila de boletos
- Liquidar pagamentos na ordem de agendamento

## Pilha e fila

O **extrato** e uma pilha (LIFO). Cada deposito, saque, PIX ou boleto pago entra no
topo com `append`, e o estorno sempre desfaz a ultima transacao com `pop()` — a
ultima que entrou e a primeira que sai.

A **fila de boletos** e uma fila (FIFO). Um boleto agendado entra no fim da lista com
`append`, e a liquidacao paga sempre o primeiro da fila com `pop(0)` — o primeiro que
entrou e o primeiro que sai. Se um boleto nao couber no saldo, a liquidacao para nele
e os seguintes continuam agendados.

## Como executar

```
python3 main.py
```
