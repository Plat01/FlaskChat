from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return open("templates/chat.html")


if __name__ == '__main__':
    app.run()
