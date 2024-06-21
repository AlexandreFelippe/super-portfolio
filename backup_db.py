import mysql.connector

config = {
    "user": "root",
    "password": "password",
    "host": "127.0.0.1",
    "database": "super_portfolio_database",
}


def export_table_to_sql(table_name, filename):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Consulta para recuperar os dados da tabela especificada
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Obter os nomes das colunas
        column_names = [i[0] for i in cursor.description]

        # Gerar script SQL de inserção
        with open(filename, "w") as f:
            for row in rows:
                # Formatar a linha para inserção SQL
                values = ", ".join(
                    [
                        f"'{value}'" if isinstance(value, str) else str(value)
                        for value in row
                    ]
                )
                columns = ", ".join(column_names)
                insert_statement = f"""INSERT INTO {table_name} ({columns})
                                   VALUES ({values});\n"""
                f.write(insert_statement)

        print(f"Dados da tabela '{table_name}' exportados para {filename}.")

    except mysql.connector.Error as e:
        print(f"Erro ao exportar dados para SQL: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão fechada.")


# Listar as tabelas que você deseja exportar
tables = ["projects_certificate",
          "projects_certificate_profiles",
          "projects_certifyinginstitution",
          "projects_profile",
          "projects_project"
          ]

# Exportar dados de cada tabela para um arquivo SQL separado
for table in tables:
    filename = f"{table}_seed.sql"
    export_table_to_sql(table, filename)
