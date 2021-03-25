import psycopg2


class Connection:
    def __init__(self, db_user: str, db_password: str, db_name: str, db_host='127.0.0.1', db_port='5432'):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def create_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_name,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
            print('Connection successful')
        except psycopg2.OperationalError as e:
            print(f'Error{e}')
        return connection

    @staticmethod
    def create_database(connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")




connection = Connection(input('Введите имя пользователя:\n'),input("Введите пароль:\n"), input("Введите базу данных"))
create_database_query = "CREATE DATABASE productes"
new_database_name= create_database_query.split(' ',maxsplit=2)
print(new_database_name[2])
connection.create_database(connection.create_connection(), create_database_query)
con_new=input('Подключиться к новой базе данных?"yes/no"\n')
if con_new=='yes' or 'y':
     
