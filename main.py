# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

import g4f
from g4f.Provider import (
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    H2o,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Ylokh,
    You,
    Yqcloud,
)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':

            # Set with provider
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": "I have products: [{ 'length': 1, 'width': 1, 'height': 1 }, { 'length': 1, 'width': 1, 'height': 1 } ] And boxes: {'id': 1, 'length': 8.56, 'width': 5.44, 'height': 1.75} {'id': 2, 'length': 11.25, 'width': 8.75, 'height': 6} {'id': 3, 'length': 14.125, 'width': 12, 'height': 3.5} {'id': 4, 'length': 12.25, 'width': 12, 'height': 6} {'id': 5, 'length': 14.875, 'width': 5.25, 'height': 7.375} {'id': 6, 'length': 13.875, 'width': 12, 'height': 2.875} {'id': 7, 'length': 12.25, 'width': 12, 'height': 6} {'id': 8, 'length': 8.75, 'width': 5.94, 'height': 0.875} {'id': 9, 'length': 10.75, 'width': 6.25, 'height': 6.25} {'id': 10, 'length': 11.5, 'width': 8.5, 'height': 5.5} {'id': 11, 'length': 12.25, 'width': 9.75, 'height': 6.25} {'id': 12, 'length': 13.5, 'width': 11.75, 'height': 6.25} What is the most optimal box? Reply without follow-up questions and comments. Reply only with box id, no letters."}],
            )

            # Convert the generator to a list
            response_messages = list(response)
            
            data = {"message": response_messages}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server():
    port = 5000
    server_address = ('', port)

    with HTTPServer(server_address, SimpleHTTPRequestHandler) as httpd:
        print(f'Starting server on port {port}...')
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
