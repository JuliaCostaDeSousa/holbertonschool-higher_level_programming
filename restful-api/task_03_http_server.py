#!/usr/bin/python3
"""
Module task_03_http_server
"""
import http.server
import json

class APIServer(http.server.BaseHTTPRequestHandler):
    """
    Subclass of http.server.BaseHTTPRequestHandler
    """

    def do_GET(self):
        """
        Handles GET requests
        """

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    PORT = 8000
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, APIServer)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()
