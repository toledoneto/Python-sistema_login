from bottle import route, run, request, template, get, static_file, error

# static routes - serverm para redirecionar para pastas e/ou pag específicas no diretório
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@route ('/login')
def login():
	return template('login')

def check_login(username, password):
	d = {'toledo':'abc123', 'camille':'123abc'}
	if username in d.keys() and d[username] == password:
		return True
	return False

@error(404)
def error404(error):
	return template('pagina404')

@route ('/login', method = 'POST')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso = check_login(username, password), nome = username)

if __name__ == '__main__':
	run(host = 'localhost', port = 8080, debug = True, reloader = True)
	# reloader = True faz com que n seja necessário reiniciar o server a cada tentativa de modificação