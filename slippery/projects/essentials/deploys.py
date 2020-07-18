import subprocess

from slippery.projects import models
from slippery import settings


class ProjectDeployer:
    def __init__(self, project: models.Project):
        self.project: models.Project = project
        self.cwd = f'{settings.PROJECTS_DIRECTORY}/{self.project.title}'


    def deploy(self):
        subprocess.run("docker-compose", "build", cwd=self.cwd)
        models.ProjectLog.objects.create(project=self.project,
                                         level=ProjectLog.LEVEL_INFO,
                                         text='Docker containers built.')
        subprocess.run("docker-compose",
                       "-f",
                       "docker-compose-production.yml",
                       "up",
                       "-d"
                       cwd=self.cwd)
        models.ProjectLog.objects.create(project=self.project,
                                         level=ProjectLog.LEVEL_INFO,
                                         text='Running Docker containers in detached mode.')
    
    def update(self):
        subprocess.run("docker-compose", "build", cwd=self.cwd)
        models.ProjectLog.objects.create(project=self.project,
                                         level=ProjectLog.LEVEL_INFO,
                                         text='Docker containers updated.')
        subprocess.run("docker-compose",
                       "-f",
                       "docker-compose-production.yml",
                       "up",
                       "--no-deps",
                       "-d",
                       cwd=self.cwd)
        models.ProjectLog.objects.create(project=self.project,
                                         level=ProjectLog.LEVEL_INFO,
                                         text='Docker containers restarted.')
    
    def check_deployability(self):
        """
        Ensure that Dockerfile and docker-compose exists.
        """
        pass
