# Documentação do Projeto de Cotação de Moedas

# Convesor de dolar para o real

Este é um pequeno script em Python que consulta a cotação atual do dólar em relação ao real usando uma API.

## Descrição

Este projeto consiste em um conjunto de scripts Python que se conectam a um banco de dados MySQL para armazenar e recuperar a cotação do dólar (USD) em relação ao real (BRL) utilizando uma API externa. O projeto inclui funções para estabelecer a conexão com o banco de dados, inserir dados, selecionar dados e fechar a conexão.

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Matheus060724/valor_USD_para_real.git

## Dependências

- `mysql-connector-python`: Para conectar e interagir com o banco de dados MySQL.
- `requests`: Para fazer requisições HTTP à API de cotação.
- `pandas`: Para manipulação e análise de dados.

## Estrutura do Código

### 1. Conexão com o Banco de Dados

```python
import mysql.connector
from mysql.connector import Error

def ConnecetDataBase():
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Esta função tenta se conectar ao banco de dados especificado usando as credenciais fornecidas.
    Se a conexão for bem-sucedida, uma mensagem de sucesso é exibida. Caso contrário, um erro é
    capturado e exibido.

    Returns:
        Connection: Um objeto de conexão ao banco de dados se a conexão for bem-sucedida; 
                    caso contrário, retorna None.
    """
    # Código para estabelecer a conexão...
```

### 2. coleta de valores

```python
import requests
from datetime import datetime
 
def Values(connectiondatabase):
    """
    Insere o valor da cotação do USD em relação ao BRL no banco de dados.

    Esta função faz uma requisição à API para obter a cotação atual do USD em relação ao BRL
    e insere esses dados no banco de dados na tabela 'valores'. A data e hora da cotação também
    são registradas.

    Args:
        connectiondatabase: Objeto de conexão com o banco de dados MySQL.

    Returns:
        None
    """
    # Código para inserir os dados...
```

### 3. seleção de dados

```python
import pandas as pd

def SelectDataBase(connectiondatabase):
    """
    Seleciona todos os registros da tabela 'valores' no banco de dados.

    Esta função executa uma consulta SQL para selecionar todos os dados da tabela 'valores'
    e os armazena em um DataFrame do pandas. Se ocorrer um erro durante a execução da consulta,
    ele será capturado e exibido.

    Args:
        connectiondatabase: Objeto de conexão com o banco de dados MySQL.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados selecionados da tabela 'valores'.
                      Retorna None se ocorrer um erro durante a seleção.
    """
    # Código para selecionar os dados...
```

### 4. Fechamento da Conexão

```python
def CloseDataBase(connectiondatabase):
    """
    Fecha a conexão com o banco de dados MySQL.

    Esta função verifica se a conexão com o banco de dados está ativa e, se estiver,
    fecha a conexão. Se ocorrer um erro ao fechar a conexão, ele será capturado e exibido.

    Args:
        connectiondatabase: Objeto de conexão com o banco de dados MySQL.

    Returns:
        None
    """
    # Código para fechar a conexão...
```



