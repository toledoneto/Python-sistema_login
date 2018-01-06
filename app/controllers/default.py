from bottle import request, template, static_file
from app import app

# static routes - serverm para redirecionar para pastas e/ou pag específicas no diretório
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@app.route ('/')
def login():
	return template('login')

@app.route('/cadastro')
def cadastro():
	return template('cadastro')

@app.route('/cadastro', method = 'POST')
def acao_cadastro():
	username = request.forms.app.get('username')
	password = request.forms.app.get('password')
	insert_user(username, password)
	return template('verificacao_cadastro', nome = username)

@app.error(404)
def error404(error):
	return template('pagina404')

@app.route ('/', method = 'POST')
def acao_login():
	username = request.forms.app.get('username')
	password = request.forms.app.get('password')
	return template('verificacao_login', sucesso = True)