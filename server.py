import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please don't forget to type the port like this \"./server 8080\"")
        quit()

    port = sys.argv[1]

    try:
        port = int(port)
    except:
        print("Please Enter a valid Port")
        quit()

    os.chdir('.')
    # Create server object listening the port 80
    server_object = HTTPServer(server_address=('', port), RequestHandlerClass=CGIHTTPRequestHandler)
    # Start the web server
    server_object.serve_forever()
    print("Running on :" + str(port))
