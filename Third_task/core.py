from http.server import HTTPServer, CGIHTTPRequestHandler
server_place = ("", 8000)
httpd = HTTPServer(server_place, CGIHTTPRequestHandler)
httpd.serve_forever()
