from flask import Flask, request
from tarefa import *

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return{
        'message': 'Api tá pokando'
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    # link = 'https://www.google.com'
    # return redirect("https://www.google.com")
    return tarefas

@app.route('/api/tarefa/<int:todo_id>', methods=['GET'])
def get_tarefa(todo_id):
    tarefa = buscar_tarefa(todo_id)
    return tarefa

@app.route('/api/tarefas', methods=['POST'])
def create_tarefa():
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')
    criar_tarefa(tarefa_name, tarefa_description)
    return {
        'message': 'Tarefa cadastrada'
    }

@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    apagar_tarefa(tarefa_id)
    return {
        'message': 'Tarefa apagada com sucesso'
    }

# Se for o modulo principal roda o projeto em debug(atualiza o projeto simultaneamente)
if __name__ == '__main__':
    app.run(debug = True)
