from django.test import TestCase

from slippery.contrib.databases.databases.dbmanager import ProjectDatabaseManager


class ProjectDatabaseManagerTestCase(TestCase):
    def test_list_databases(self):
        dbmanager = ProjectDatabaseManager()
        databases = dbmanager.list_databases()
        self.assertEqual(type(databases), list)
