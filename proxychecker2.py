from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class ProxyChecker(BaseHTTPRequestHandler):

    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        if self.path == '/':
            with open('proxy_checker.html', 'r') as file:
                self._send_response(file.read())
        else:
            self._send_response("404 - Not Found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        proxy_list = post_data.split("\n")
        checked_proxies = []
        for proxy in proxy_list:
            try:
                response = requests.get('http://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
                if response.status_code == 200:
                    checked_proxies.append((proxy, 'valid'))
                else:
                    checked_proxies.append((proxy, 'invalid'))
            except:
                checked_proxies.append((proxy, 'invalid'))
        with open('checked_proxies.html', 'r') as file:
            checked_proxies_template = file.read()
            checked_proxies_table = ""
            for proxy in checked_proxies:
                checked_proxies_table += "<tr><td>{}</td><td>{}</td></tr>".format(proxy[0], proxy[1])
            self._send_response(checked_proxies_template.replace("{checked_proxies}", checked_proxies_table))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ProxyChecker)
    print('Starting server...')
    httpd.serve_forever()

run()
