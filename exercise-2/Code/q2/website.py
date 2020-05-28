import re

import http.server
from http.server import BaseHTTPRequestHandler

from functools import partial

class Response:
    def __init__(self):
        self.status_code    = 404
        self.text           = ''

class CDataConverter():
    @staticmethod
    def getBytesFromString(str, encoding = 'utf-8'):
        return bytes(str.encode(encoding))

class CHandler(BaseHTTPRequestHandler):
    def __init__(self, routes_no_params, routes_with_params, *args):
        self.routes_no_params       = routes_no_params
        self.routes_with_params     = routes_with_params
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def sendPageDataHTML(self, status_code, bytes_data):
        data = CDataConverter.getBytesFromString(bytes_data)
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Charset', 'UTF-8')
        self.send_header('Content-Length', len(data))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        response = Response()
        response.status_code, response.text = self.route_request(self.path)
        self.sendPageDataHTML(response.status_code, response.text)
    
    def route_request(self, path):
        response = Response()        
        route_tokes = list(filter(None, path.split('/')))
        if 2 > len(route_tokes):  
            for r in self.routes_no_params.keys():
                if r == path:
                    f = self.routes_no_params[path]             
                    response.status_code, response.text = f()
        elif 2 == len(route_tokes):
            route_name, route_param_value = route_tokes
            for r in self.routes_with_params.keys():
                if r == route_name:
                    (f, route_param_regexp) = self.routes_with_params[route_name]             
                    params_groups = re.search(route_param_regexp, route_param_value).groups()
                    if params_groups is not None:
                        response.status_code, response.text = f(*params_groups)                        
        return response.status_code, response.text

class Website:
    routes_no_params    = {}
    routes_with_params  = {}
    
    def route(self, path):
        def wrap(f):
            route_tokes = list(filter(None, path.split('/')))
            if 2 > len(route_tokes):                
                self.routes_no_params[path] = f
            elif 2 == len(route_tokes):
                route_name, route_param_regexp = route_tokes
                self.routes_with_params[route_name] = (f, route_param_regexp)
            return f
        return wrap
    
    def run(self, address): 
        server_ip_str, server_port_int  = address
        server_handler = partial(CHandler, self.routes_no_params, self.routes_with_params)
        http_server = http.server.HTTPServer((server_ip_str, server_port_int), server_handler)
        http_server.serve_forever()
        