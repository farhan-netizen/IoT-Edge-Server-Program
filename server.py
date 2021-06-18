import http.server
import socketserver
import requests
import os, random
import json
import pandas as pd


PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        # - request -
      # will use content_length to verify success case.
        content_length = int(self.headers['Content-Length'])

        # We generate a Random number between 1 and 100, if the number is greater than 80
        # we return error reponse, this is to randomly show failure in 20% of the probable cases
        rnd = random.randrange(1, 100, 1)
     
        if rnd > 80:
            # Failure Case
             self.send_response(400)
             self.send_header('Content-type', 'text/json')
             self.end_headers()

             output_data = {'status': 'Failure', 'result': 'Bad Request - Validation Error'}
             output_json = json.dumps(output_data)
        
             self.wfile.write(output_json.encode('utf-8'))
        else:
            # Success Case
            if content_length:
                input_json = self.rfile.read(content_length)
    
                input_data = json.loads(input_json)
                jsn = pd.DataFrame(input_data, index=[0])
                print(jsn)
                jsn.to_csv("response.csv", mode='a', header=False, index=False)
            else:
                input_data = None
    
            # - response -
    
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
    
            output_data = {'status': 'OK', 'result': 'Data saved'}
            output_json = json.dumps(output_data)
            
            self.wfile.write(output_json.encode('utf-8'))

Handler = MyHandler

def serverapp():
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Starting http://127.0.0.1:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping by Ctrl+C")
        httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
        
if __name__ == '__main__':
    serverapp()