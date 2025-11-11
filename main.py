from flask import Flask, redirect
from tarefa import buscar_tarefas, buscar_tarefa

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return{
        'message': 'Api rodando'   
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    # link = 'https://www.google.com'
    # return redirect("https://www.gogle.com")
    return tarefas

@app.route('/api/tarefa/<int:todo_id>', methods=['GET'])
def get_tarefa(todo_id):
    tarefa = buscar_tarefa(todo_id)
    return tarefa

# Se for o modulo principal roda o projeto em debug(atualiza o projeto simultaneamente)
if __name__ == '__main__':
    app.run(debug = True)
