#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir('/workspaces/OdderHyt.royensmojsite.io')
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
