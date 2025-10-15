from flask import Flask
from tarefa import buscar_tarefas

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'message': 'API tá pokando'
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

# Se for o módulo principal roda o projeto em debug
if __name__ == '__main__':
    app.run(debug=True)