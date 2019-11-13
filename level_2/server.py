from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import __init__
import os
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def do_POST(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "The server will process the unprocceded data"
        # Write content as utf-8 data


        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        my_json = post_data.decode('utf8')

        print(my_json.replace('{"communication": "','').replace('"}',''))
        read_data = my_json.replace('{"communication": "','').replace('"}','')
        new = ""
        filename = f'./processed/communication-{{}}.json'.format(read_data.split("|")[0][3:len(read_data)])

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        for data in read_data.split("|"):
            if(len(new) == 0):
               new =  new+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])
            else:
               new =  new+','+str(data.split('=')[:1]) + ':' +str(data.split('=')[1:2])

        data_clean =str ('{'+new.replace("[","").replace("]","").replace('"',"")+'}')
        json_string = (json.dumps(eval(data_clean), indent=4))
        with open(filename, 'w') as file:
            file.write(json_string.replace('"',"'"))

        return
def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()