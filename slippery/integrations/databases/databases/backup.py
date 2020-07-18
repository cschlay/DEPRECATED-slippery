import subprocess

from slippery.database import models
from slippery import settings


class DatabaseBackup:
    def __init__(self, database: models.Database):
        self.database: models.Database = database

    def take_snapshot(self, snapshot_title: str):
        location = f"{settings.DATABASE_SNAPSHOT_DIRECTORY}/{self.database.name}/{snapshot_title}"
        subprocess.run(["pg_dump", self.database.name, ">", snapshot_title],
                       cwd=location)
        models.Snapshot.objects.create(title=snapshot_title,
                                       database=self.database,
                                       location=location)
