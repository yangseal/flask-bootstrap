def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


if __name__=='__main__':
    from wsgiref.simple_server import  make_server
    httpd = make_server('0.0.0.0', 8001, application)
    print('httpd run on:'+str(httpd.server_port))
    httpd.serve_forever()