# Flask Examples

## Criar o ambiente virtual

Criar o ambiente virtual

```bash
python3 -m venv .venv
```

## Ativar o ambiente virtual

Ativar o ambiente virtual no Linux

```bash
. .venv/bin/activate
```

Ativar o ambiente virtual no Windows (Power Shell, GitBash)

```bash
.venv\Scripts\activate
```

ou

```bash
.venv\Scripts\activate.bat
```

## Instalar o Flask

```bash
pip install Flask
```


## Gerar o arquivo requirements.txt

```bash
pip freeze > requirements.txt
```

## Ignorar diretório .venv

Garantir que o diretório `.venv` está configurado para ser ignorado pelo git, arquivo `.gitignore`:

https://github.com/github/gitignore/blob/main/Python.gitignore
