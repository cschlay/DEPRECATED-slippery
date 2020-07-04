import getpass

def create_dotenv_file():
    with open('.env', 'w') as file:
        pass


def create_nginx_config():
    with open('scripts/nginx-template.txt', 'r') as readfile:
        content: str = readfile.read()
        server_name = input('Server domain or IP: ')
        config = {
            'server_name': server_name,
            'user': getpass.getuser()
        }
        result = content.format(**config).replace('\[','{').replace('\]', '}')
        with open(f'scripts/nginx/slippery', 'w') as writefile:
            writefile.write(result)


def create_systemd_service():
    with open('scripts/slippery.service.txt', 'r') as readfile:
        content: str = readfile.read()

        config = {
            'user': getpass.getuser()
        }
        result: str = content.format(**config)

        with open('scripts/slippery.service', 'w') as writefile:
            print(result)
            writefile.write(result)


def main():
    create_systemd_service()
    create_nginx_config()


if __name__ == '__main__':
    main()
