import docker


def run(command, container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    exit_code, output = container.exec_run(command)