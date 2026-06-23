# Desafio b2bflow

## Descrição

Aplicação em Python que busca contatos armazenados no Supabase e envia mensagens personalizadas via WhatsApp utilizando a Z-API.

Mensagem enviada:

Olá, <nome_contato> tudo bem com você?

## Tecnologias

* Python 3
* Supabase
* Z-API
* Requests
* Python Dotenv

## Estrutura da Tabela

Tabela: `contatos`

| Campo    | Tipo    |
| -------- | ------- |
| id       | integer |
| nome     | text    |
| telefone | text    |

```sql
CREATE TABLE contatos (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL
);
```

## Variáveis de Ambiente

Crie um arquivo `.env`:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Fluxo da Aplicação

1. Busca até 3 contatos no Supabase.
2. Personaliza a mensagem utilizando o nome do contato.
3. Envia a mensagem via Z-API.
4. Registra sucesso ou falha de cada envio.

## Exemplo de Mensagem

```text
Olá, Pedro tudo bem com você?
```
