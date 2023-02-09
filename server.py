import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import socket
import threading
import webbrowser
import time

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

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    url = "http://" + str(ip_address) + ":" + str(port)
    os.chdir('.')

    def start_server():
        server_object = HTTPServer(server_address=(ip_address, port), RequestHandlerClass=CGIHTTPRequestHandler)
        print("Running on " + url)
        server_object.serve_forever()


    x = threading.Thread(target=start_server, args=())
    x.start()
    webbrowser.open_new(url)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)
