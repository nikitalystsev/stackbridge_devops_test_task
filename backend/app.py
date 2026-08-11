from http.server import HTTPServer, BaseHTTPRequestHandler

# Класс-обработчик входящих запросов
class MyHandler(BaseHTTPRequestHandler):
    # обработка get-запросов
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))


def main():

    host_name = ""
    server_port = 8080

    my_server = HTTPServer((host_name, server_port), MyHandler)

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")

    my_server.server_close()


if __name__ == "__main__":
    main()
