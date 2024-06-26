import subprocess


def executa_comando(comando):
    resultado = subprocess.run(
        comando, shell=True, capture_output=True, text=True
    )
    if resultado.returncode == 0:
        return True
    else:
        print(f"Erro ao executar o comando: {resultado.stderr}")
        return False


def recupera_dados():
    usuario = "root"
    senha = "password"
    banco_dados = "super_portfolio_database"
    container_name = "super-portfolio-mysql-container"
    arquivos = [
        "clear_tables",
        "projects_certifyinginstitution_seed",
        "projects_certificate_seed",
        "projects_project_seed",
        "projects_profile_seed",
        "projects_certificate_profiles_seed",
    ]

    base_path = "/home/alexandre/python/projetos/python-033-python-projeto-super-portfolio/sedeers/" # noqa

    for arquivo in arquivos:
        caminho_arquivo = f"{base_path}{arquivo}.sql"

        try:
            with open(caminho_arquivo, "r"):
                pass
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            continue

        comando = (
            f"docker exec -i {container_name} mysql -u {usuario} -p{senha} {banco_dados} < {caminho_arquivo}" # noqa
        )
        if executa_comando(comando):
            print(f"Arquivo {arquivo} importado com sucesso.")
        else:
            print(f"Erro ao importar o arquivo {arquivo}.")


recupera_dados()
