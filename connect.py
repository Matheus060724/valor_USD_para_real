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
    try:
        # Tenta estabelecer a conexão com o banco de dados
        Connection = mysql.connector.connect(
            user = "root",
            password = "*********",
            host = "localhost",
            database = "test_cotacao"
        )
        
        # Mensagem de sucesso na conexão
        print("Conexão com Sucesso!")

    except Error as e:
        # Captura e exibe erros que ocorrem durante a tentativa de conexão 
        print(f"Erro ao conectar com o banco de dados: {e}")

    else:
        return Connection
