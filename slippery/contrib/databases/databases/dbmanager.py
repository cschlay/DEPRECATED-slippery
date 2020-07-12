import psycopg2
from psycopg2 import sql

from slippery import settings


class ProjectDatabaseManager:
    """
    Manages the main app database, that projects might be using.
    """

    def list_databases(self):
        """Returns a list of database names."""
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT datname FROM pg_database 
                WHERE datistemplate=false and datname<>'postgres'
        """)
        result = cursor.fetchall()
        connection.close()
        return list(map(lambda row: {'name': row[0]}, result))

    def create_database(self, name):
        connection = self._connect()
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(name))
        )
        connection.close()
        return True

    def delete_database(self, name):
        if name != 'postgres':
            connection = self._connect()
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(
                sql.Identifier(name))
            )
            connection.close()
            return True
        return False

    @staticmethod
    def _connect():
        return psycopg2.connect(
            host=settings.APP_DB_HOST,
            port=settings.APP_DB_PORT,
            user=settings.APP_DB_USER,
            password=settings.APP_DB_PASSWORD
        )
