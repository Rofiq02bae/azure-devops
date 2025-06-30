from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Azure Flask!'
    return 'Halo dari CI/CD GitHub + Azure 💙'


if __name__ == '__main__':
    app.run()
