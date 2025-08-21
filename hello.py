from flask import Flask, request

app = Flask(__name__);

@app.route('/')
def index():
    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/user/Eduarda%20Cristovao/PT3033171/IFSP">Identificação</a></li>
        <li><a href="/contextorequisicao">Contexto da Requisição</a></li>
    </ul>
    ''';

@app.route('/user/<name>/<prontuario>/IFSP')
def identificacao(name, prontuario):
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: {name}</h2>
    <h2>Prontuário: {prontuario}</h2>
    <h2>Instituição: IFSP</h2>
    <p><a href="/">Voltar</a></p>
    ''';

@app.route('/contextorequisicao')
def contextorequisicao():
    
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.host
    
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O IP do cumputador remoto é: {ip}</h2>
    <h2>O host da aplicação é: {host}</h2>
    <p><a href="/">Voltar</a></p>
    ''';

