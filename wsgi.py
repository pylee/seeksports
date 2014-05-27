from bottle import route, run

def application(environ, start_response):
     status = '200 OK'
     response_headers = [('Content-type','text/plain')]
     start_response(status, response_headers)
     return ['Hello World']


@route('/hello')
def hello():
	return "Hello World! from bottle"

run(host='0.0.0.0', port=8080, debug=True)
