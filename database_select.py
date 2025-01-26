import connect
import pandas as pd
from mysql.connector import Error


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
     
    # Cria um cursor para executar comandos SQL
    Cursor = connectiondatabase.cursor()

    try:
        # Consulta SQL para selecionar todos os registros da tabela 'valores'
        CodeSQL = "SELECT * FROM test_cotacao.valores;"
        Cursor.execute(CodeSQL) # Executa a consulta SQL com os dados obtidos da API
        Answer = Cursor.fetchall() # Obtém todos os resultados da consulta

        # Cria um DataFrame do pandas a partir dos dados obtidos
        df = pd.DataFrame(data = Answer,
                        columns=(["ID", "Valor", "Data"]))
    
    # Captura e exibe erros relacionados à execução da consulta SQL
    except Error as e:
        print(f"Erro ao selecionar os dados: {e}")

    # Fecha o cursor se a conexão estiver ativa
    finally:
        if connectiondatabase.is_connected():
            Cursor.close()
    
    return df # Retorna o DataFrame com os dados selecionados


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

# Seleciona os valores da cotação no banco de dados
print(SelectDataBase(ConnectionDataBase))

# Encerra a conexão com o banco de dados
CloseDataBase(ConnectionDataBase)
