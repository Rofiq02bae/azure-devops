from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Azure Flask! & Halo dari CI/CD GitHub + Azure 💙'
    return ''


if __name__ == '__main__':
    app.run()
