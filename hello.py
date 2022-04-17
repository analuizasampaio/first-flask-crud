from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Salve Ingrid!"

@app.route("/ana")
def ana():
    return "Ana luiza"

database = {}
database['ALUNO'] = [
                        {
                            "id": 2,
                            "nome": "Vitor" 
                         }
                    ]
database['PROFESSOR'] = []

@app.route('/todos')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])   

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno_requisitado = request.json
    database['ALUNO'].append(novo_aluno_requisitado)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in (database['ALUNO']):
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'aluno não encontrado', 404

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
    for aluno in (database['ALUNO']):
        if aluno['id'] == id_aluno:
            posicao_aluno = database['ALUNO'].index(aluno)
            database['ALUNO'].pop(posicao_aluno)
            return jsonify(aluno)
    return 'aluno não encontrado', 404

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def altera_aluno(id_aluno):
    '''
        pegando aluno que está sendo enviado no body
        e guardando na variavel aluno_alterado

    '''
    aluno_alterado = request.json
    for aluno in (database['ALUNO']):
        if aluno['id'] == id_aluno:
            aluno['nome'] = aluno_alterado['nome']
            return jsonify(database['ALUNO'])
    return 'aluno não encontrado', 404
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)