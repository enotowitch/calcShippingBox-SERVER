# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            data = {"message": "Hello from the server!"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # This allows requests from any origin.
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server():
    port = 5000  # Change the server port to 5000 to match your error message.
    server_address = ('', port)

    with HTTPServer(server_address, SimpleHTTPRequestHandler) as httpd:
        print(f'Starting server on port {port}...')
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()

# todo 1