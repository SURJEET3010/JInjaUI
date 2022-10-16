from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from jinja2 import Environment, FileSystemLoader


with open("data.json", "r") as d:
    data = json.load(d)

fileloader = FileSystemLoader("template")
env = Environment(loader=fileloader)

rendered = env.get_template("JinjaUI.html").render(data=data)


class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):  # handle GET request
        self._set_headers()
        self.wfile.write(bytes(rendered, "utf8"))


def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    web = server_class(server_address, handler_class)
    print("Starting server...")
    web.serve_forever()


if __name__ == '__main__':
    run()
