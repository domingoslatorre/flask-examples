from flask import Flask, request

# Crie um aplicativo Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
app = Flask(__name__)


# Define uma rota
# Uma rota é uma URL (ou caminho) para o aplicativo
# Quando o usuário acessa a URL, a função associada é executada
# A função retorna o conteúdo que será exibido na página
@app.route('/')
def hello_world():
    return 'Hello, World!!!!'


@app.route('/quem-somos')
def quem_somos():
    return 'Quem somos'


# A função pode retornar diferentes conteúdos com base no cabeçalho da solicitação
# O cabeçalho da solicitação contém informações sobre o navegador do usuário
# e as preferências de idioma
@app.route('/servicos')
def servicos():
    language = request.headers.get('Accept-Language')
    if language.startswith('pt'):
        return 'Nossos serviços'
    else:
        return 'Our services'
    

servicos = {
    1: 'Corte de cabelo',
    2: 'Manicure',
    3: 'Pedicure',
    4: 'Maquiagem'
}

# A função pode receber parâmetros da URL
# O parâmetro é passado para a função como um argumento
# O valor passado é convertido para o tipo especificado e
# utilizado na função para retornar o conteúdo apropriado
@app.route('/servicos/<int:id>')
def servico(id):
    if id in servicos:
        return servicos[id]
    else:
        return 'Serviço não encontrado', 404

# Se o módulo for executado diretamente, execute o aplicativo
if __name__ == '__main__':
    app.run()
    # Ative o modo de depuração para atualizar automaticamente o aplicativo quando você fizer alterações
    #  app.run(debug=True)  
