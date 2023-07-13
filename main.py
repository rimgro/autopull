import os
import subprocess

from flask import Flask, request
import json



def execute_command(command):
    try:
        subprocess.check_output(command)
        print('Command executed successfully')
    except subprocess.CalledProcessError as e:
        print('Error executing command:', e.output)


# Загрузка данных из файла конфига
with open(os.path.dirname(os.path.abspath(__file__)) + '/config.json') as file:
    config_data = json.load(file)

port = config_data.get("port", 12345)
webhook_route = config_data.get("webhook_route", "/webhook")
action = config_data.get("action", [])
repo_path = config_data.get("path", "")

app = Flask(__name__)


@app.route(webhook_route, methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json  # Получаем данные из запроса
        # Выполните необходимые действия здесь, например, выполните команду git pull
        # для загрузки последних изменений репозитория
        print(fr"Получен вебхук из репозитория {payload['repository']['name']} от {payload['pusher']['name']}")
        os.chdir(repo_path)
        execute_command(action)

    return "Webhook recivied"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)