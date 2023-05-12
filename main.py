from flask import Flask, request


app = Flask(__name__)

@app.route('/testwebhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json  # Получаем данные из запроса
        # Выполните необходимые действия здесь, например, выполните команду git pull
        # для загрузки последних изменений репозитория
        print(payload)
        return 'Webhook received successfully'  # Ответите на запрос от GitHub

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12354)