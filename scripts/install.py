import getpass
from django.core.management.utils import get_random_secret_key


def create_dotenv_file(server_name):
    with open('scripts/.env-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'hostname': server_name,
            'secret_key': get_random_secret_key()
        }
        result: str = content.format(**config)
        with open('.env', 'w') as writefile:
            writefile.write(result)


def create_sudoers_config():
    with open('scripts/sudoers-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'user': getpass.getuser()
        }
        result: str = content.format(**config)

        with open('scripts/files/sudoers-slippery', 'w') as writefile:
            writefile.write(result)


def create_nginx_config(server_name):
    with open('scripts/nginx-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'server_name': server_name,
            'user': getpass.getuser()
        }
        result: str = content.format(**config).replace('\[','{').replace('\]', '}')
        with open(f'scripts/files/nginx-site-slippery', 'w') as writefile:
            writefile.write(result)


def create_systemd_service():
    with open('scripts/slippery.service.txt', 'r') as readfile:
        content: str = readfile.read()

        config = {
            'user': getpass.getuser()
        }
        result: str = content.format(**config)

        with open('scripts/slippery.service', 'w') as writefile:
            writefile.write(result)


def main():
    server_name = input('Server domain or IP: ')
    create_systemd_service()
    create_nginx_config(server_name)
    create_dotenv_file(server_name)


if __name__ == '__main__':
    main()
