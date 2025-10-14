from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'message': 'API tá pokando'
    }

# Se for o módulo principal roda o projeto em debug
if __name__ == '__main__':
    app.run(debug=True)