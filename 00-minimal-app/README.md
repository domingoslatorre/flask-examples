# 00 Minimal App

## Objetivos

* Como criar uma app Flask
* Como ativar o modo debug para live reload
* Para que serve o PIN (Personal Identification Number) exibido no terminal
* Fazer requisições HTTP por meio do navegador e também por meio de programas como o postman
* Conceitos do HTTP
  * Client/Server
  * Stateless
  * Version
* Request
  * Method (GET)
  * URI
  * Version
  * Headers
  * Body
* Response
  * Status Code
  * Headers
  * Body


## Instruções

### Como executar a aplicação flask

Com o ambiente virtual ativado executar:

```bash
flask --app 00-minimal-app/app.py run

```

Se o módulo for executado diretamente.

```python
if __name__ == '__main__':
    app.run()

```

```bash
python3 00-minimal-app/app.py
```

### Executar em modo debug

```bash
flask --app 00-minimal-app/app.py run --debug
```

O PIN exibido será solicitado caso você tente acessar a aplicação de um endereço IP diferente do local onde a aplicação está sendo executada