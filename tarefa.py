from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitação',
            'descricao': 'Vamos aprender a digitar',
            'status': 'Ativo'
        },
        {
            'id': 2,
            'nome': 'Aprender Python',
            'descricao': 'Aprender python para programar',
            'status': 'Pendente'
        }
    ]
    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
        'id': 1,
        'nome': 'Aprender digitação',
        'descricao': 'Vamos aprender a digitar',
        'status': 'Ativo'
    }
    return jsonify(tarefa)
