from django.test import TestCase

from slippery.integrations.databases.databases.dbmanager import ProjectDatabaseManager


class ProjectDatabaseManagerTestCase(TestCase):
    def test_list_databases(self):
        dbmanager = ProjectDatabaseManager()
        databases = dbmanager.list_databases()
        self.assertEqual(type(databases), list)

    def test_create_database(self):
        dbmanager = ProjectDatabaseManager()
        result1 = dbmanager.create_database('testdb')
        self.assertTrue(result1)
        result2 = dbmanager.delete_database('testdb')
        self.assertTrue(result2)
