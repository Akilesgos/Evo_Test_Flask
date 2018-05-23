import psycopg2


class UseDatabase():
    def __init__(self, dbname, user, password) -> 'None':
        self.dbconfig = {}
        self.dbconfig['dbname'] = dbname
        self.dbconfig['user'] = user
        self.dbconfig['password'] = password
    try:
        def __enter__(self) -> 'cursor':
            self.connect = psycopg2.connect(
                'dbname={dbname} user={user} password={password}'.format(
                    dbname=self.dbconfig['dbname'],
                    user=self.dbconfig['user'],
                    password=self.dbconfig['password']))
            self.cursor = self.connect.cursor()
            return self.cursor
    except psycopg2.Error as err:
        raise ConnectionError(err)
    except psycopg2.OperationalError as err:
        raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> 'None':
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass
