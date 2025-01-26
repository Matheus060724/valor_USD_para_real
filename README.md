# Documentação do Projeto de Cotação de Moedas

## Descrição

Este projeto consiste em um conjunto de scripts Python que se conectam a um banco de dados MySQL para armazenar e recuperar a cotação do dólar (USD) em relação ao real (BRL) utilizando uma API externa. O projeto inclui funções para estabelecer a conexão com o banco de dados, inserir dados, selecionar dados e fechar a conexão.

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
