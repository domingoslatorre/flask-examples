from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Como trabalhar com templates no Flask

# O que são templates?
# Templates são arquivos que contêm código HTML e permitem a inserção de dados dinâmicos
# Exemplos de dados dinâmicos:
#     - Variáveis
#     - Estruturas de controle (if, for)
#     - Expressões

# Lembre-se: O Flask é um microframework e não possui um mecanismo de templates embutido
# O Flask utiliza o Jinja2 como mecanismo de templates

# Como renderizar templates no Flask?
# Para renderizar um template no Flask, utilize a função "render_template"
# A função "render_template" recebe o nome do arquivo do template e os dados a serem inseridos no template
# A função "render_template" procura o arquivo do template na pasta "templates"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


tabela_produtos = {
    1: {'nome': 'Corte de cabelo', 'descricao': 'Corte de cabelo masculino ou feminino', 'preco': 50.00},
    2: {'nome': 'Manicure', 'descricao': 'Manicure com esmaltação', 'preco': 30.00},
    3: {'nome': 'Pedicure', 'descricao': 'Pedicure com esmaltação', 'preco': 50.00},
}


@app.route('/produtos', methods=['GET'])
def produtos():
    return render_template('produtos.html', produtos=tabela_produtos)


@app.route('/produtos/<int:id>', methods=['GET'])
def detalhe_produto(id):
    produto = tabela_produtos.get(id)
    if produto:
        return render_template('produto.html', produto=produto)
    else:
        return 'Produto não encontrado', 404


@app.route('/produtos/novo', methods=['GET'])
def novo_produto():
    return render_template('novo_produto.html')


@app.route('/produtos', methods=['POST'])
def salvar_produto():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = request.form.get('preco')

    id = max(tabela_produtos.keys()) + 1

    tabela_produtos[id] = {'nome': nome, 'descricao': descricao, 'preco': preco}
    
    # redirecionar para a página de detalhes do produto
    return redirect(url_for('detalhe_produto', id=id))

# Como trabalhar com arquivos estáticos no Flask

# O que são arquivos estáticos?
# Arquivos estáticos são arquivos que não são gerados dinamicamente pelo servidor
# Exemplos de arquivos estáticos:
#     - Imagens
#     - Folhas de estilo (CSS)
#     - Scripts (JavaScript)
#     - Fontes


# Como servir arquivos estáticos no Flask?
# O Flask possui uma pasta especial para arquivos estáticos
# Esta pasta é chamada de "static"
# A pasta "static" deve estar no mesmo diretório que o arquivo app.py
# Exemplo de estrutura de diretórios:
# .
# ├── app.py
# └── static
#     ├── style.css
#     └── script.js
#

# Como referenciar arquivos estáticos no HTML?
# Para referenciar arquivos estáticos no HTML, utilize o filtro "url_for"
# O filtro "url_for" gera a URL para um endpoint do Flask

# Exemplo de referência a um arquivo estático no HTML:
# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
