import time
from flask import Flask, redirect, request

app = Flask(__name__)


# Recebendo dados da request
# O objeto request contém informações sobre a solicitação HTTP que o cliente fez ao servidor.
# Podemos receber dados de x diferentes maneiras:
# Independente de método HTTP, podemos receber dados de duas maneiras:


alunos = {
    'SP001': 'Maria',
    'SP002': 'José',
    'SP003': 'Ana'
}

# 1. Parâmetros de consulta (query parameters)
# Parâmetros de consulta são pares de chave-valor na URL
# Eles são separados da URL por um ponto de interrogação (?)
# Eles são separados por um e comercial (&)
@app.route('/alunos')
def listar_alunos():
    # request.args é um dicionário que contém os parâmetros de consulta
    # request.args.get() retorna o valor do parâmetro de consulta especificado
    prontuario = request.args.get('prontuario')
    if prontuario:
        return alunos[prontuario]
    else:
        return alunos


# 2. Parâmetros de rota (route parameters)
# Parâmetros de rota são partes variáveis da URL
# Eles são especificados na rota entre colchetes <>
# Eles são passados para a função associada como argumentos
# Eles são convertidos para o tipo especificado (Se não for especificado, eles são strings)
@app.route('/alunos/<prontuario>')
def detalhe_aluno(prontuario):
    if prontuario in alunos:
        return alunos[prontuario]
    else:
        return 'Aluno não encontrado', 404
    
produtos = {
    1: {'nome': 'Corte de cabelo', 'preco': 50.00},
    2: {'nome': 'Manicure', 'preco': 30.00},
    3: {'nome': 'Pedicure', 'preco': 30.00},
}

@app.route('/produtos')
def listar_produtos():
    return produtos

# Parâmetros de rota (route parameters) com tipo de dados especificado
# caso seja passado um valor que não seja um inteiro, o Flask retornará um erro 404
@app.route('/produtos/<int:id>')
def detalhe_produto(id):
    if id in produtos:
        return f"Nome: {produtos[id]['nome']}, Preço: {produtos[id]['preco']}"
    else:
        return 'Produto não encontrado', 404

# Método POST:
# 3. Parâmetros de formulário (form parameters)
# Parâmetros de formulário são enviados no corpo da solicitação HTTP
@app.route('/produtos/novo', methods=['GET'])
def cadastrar_produto_form():
    return """
    <form action="/produtos" method="POST">
        <input type="text" name="nome" placeholder="Nome">
        <input type="text" name="preco" placeholder="Preço">
        <button type="submit">Cadastrar</button>
    </form>
"""

@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    # request.form é um dicionário que contém os parâmetros de formulário
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    
    # Salvar o produto no "banco de dados"
    produtos[len(produtos) + 1] = {'nome': nome, 'preco': preco}

    # redirecionar para a página de produtos, com status 302 (redirecionamento temporário)
    return redirect('/produtos', 302)


# 4. Corpo da solicitação (request body)
# O corpo da solicitação contém dados enviados pelo cliente
# O corpo da solicitação pode conter dados em diferentes formatos
# O formato mais comum é JSON
@app.route('/produtos-json', methods=['POST'])
def cadastrar_produto_json():
    # request.json é um dicionário que contém os dados do corpo da solicitação
    dados = request.json
    nome = dados.get('nome')
    preco = dados.get('preco')
    
    # Salvar o produto no "banco de dados"
    produtos[len(produtos) + 1] = {'nome': nome, 'preco': preco}

    # retorna o produto cadastrado e status 201 (criado) e o cabeçalho Location com a URL do produto
    return {'nome': nome, 'preco': preco}, 201, {'Location': f'/produtos/{len(produtos)}'}


# 5. Arquivos enviados (uploaded files)
@app.route('/upload', methods=['GET'])
def upload_form():
    return """
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="arquivo">
        <button type="submit">Enviar</button>
    </form>
"""

@app.route('/upload', methods=['POST'])
def upload_file():
    # request.files é um dicionário que contém os arquivos enviados
    arquivo = request.files.get('arquivo')

    # Verifica a extensão do arquivo
    if not arquivo.filename.endswith('.txt'):
        return 'Apenas arquivos .txt são permitidos', 400
    
    infos = {
        'original_filename': arquivo.filename,
        'new_filename': f"{int(time.time())}_{arquivo.filename}",
        'content': arquivo.read().decode('utf-8')
    }

    # Salva o arquivo em disco
    arquivo.save(infos['new_filename'])
    
    return f"""
        <h1>Arquivo enviado</h1>
        <p>Nome: {infos['original_filename']}</p>
        <p>Conteúdo:</p>
        <pre>{infos['content']}</pre>
        """


if __name__ == '__main__':
    app.run()
    