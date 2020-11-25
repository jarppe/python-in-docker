from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello world\n".encode("utf8"))


if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", 8080), Handler)
    httpd.serve_forever()
