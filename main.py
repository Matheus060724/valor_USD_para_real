import connect
from mysql.connector import Error
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
            Cursor = connectiondatabase.cursor()
    """

    # Cria um cursor para executar comandos SQL
    Cursor = connectiondatabase.cursor()

    # Valores para conter no banco de dados
    Date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # data e hora atual
    Url = "https://economia.awesomeapi.com.br/last/USD-BRL" # URL com o valora da cotação
    
    try:
        # Faz a requisição à API e verifica se a resposta foi bem-sucedida
        AnswerAPI = requests.get(Url)
        AnswerAPI.raise_for_status() # Levanta um erro se a requisição falhar
        Data = AnswerAPI.json() # Converte a resposta JSON em um dicionário

        # Consulta SQL para inserir os dados no banco de dados
        CodeSQL = """ INSERT INTO test_cotacao.valores (valor, data_cotacao) 
        VALUES 
            (%s, %s)
        """

        # Executa a consulta SQL com os dados obtidos da API
        Cursor.execute(CodeSQL, (Data["USDBRL"]["bid"], Date))
        # Confirma a transação no banco de dados
        connectiondatabase.commit()
    
    except requests.exceptions.RequestException as e:
        # Captura e exibe erros relacionados à requisição HTTP
        print(f"Ocorreu um erro ao fazer a requisição à API: {e}")
    
    except Error as e:
        # Captura e exibe erros relacionados à execução da consulta SQL
        print(f"Ocorreu um erro ao executar a consulta SQL: {e}")
    
    except KeyError as e:
        # Captura e exibe erros relacionados à manipulação de dicionários
        print(f"Ocorreu um erro ao acessar os dados da API: {e}")
    
    finally:
        # Fecha o cursor
        Cursor.close()


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
    try:
        # Verifica se a conexão está ativa antes de fechá-la
        if connectiondatabase.is_connected():
            # Fecha a conexão
            connectiondatabase.close()
            print("Conexão Encerrada")
    
    # Captura e exibe erros relacionados ao fechamento da conexão
    except Error as e:
        print(f"Erro ao encerrar a conexão: {e}")
    

# Estabelece a conexão com o banco de dados
ConnectionDataBase = connect.ConnecetDataBase()
# Insere os valores da cotação no banco de dados
Values(ConnectionDataBase)
# Encerra a conexão com o banco de dados
CloseDataBase(ConnectionDataBase)
