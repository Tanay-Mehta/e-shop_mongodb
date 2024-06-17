from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

class PrimeFactorsHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, response_code=200):
        self.send_response(response_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        number_str = query.get('number', [None])[0]

        self._set_headers()
        
        if number_str and number_str.isdigit():
            number = int(number_str)
            factors = prime_factors(number)
            response = f"Prime factors of {number} are {factors}"
        else:
            response = "Please provide a valid number as a query parameter, e.g., ?number=60"
        
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=PrimeFactorsHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

#// Run : python your_script_name.py
#// http://localhost:8000?number=58
#// Task: Optimise and create a new endpoint that serves an html file to access this service
