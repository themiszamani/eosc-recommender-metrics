#!/usr/bin/env python3
import sys
import time
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from functools import partial
import argparse
from pathlib import Path
import shutil



def start_server(args):
    handler = partial(SimpleHTTPRequestHandler, directory=args.output)
    httpd = HTTPServer((args.address, int(args.port)), handler)
    httpd.serve_forever()


# Main logic
def main(args=None):

    # create output folder if doesn't exist
    Path(args.output).mkdir(parents=True, exist_ok=True)
    # copy needed files
    shutil.copy("./report.html.prototype", args.output+"/index.html")
    shutil.copy(args.input+"/metrics.json", args.output)


    threading.Thread(target=start_server, args=(args,)).start()
    webbrowser.open_new("http://"+args.address+":"+args.port)
    
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

# Parse arguments and call main 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate report")
    parser.add_argument(
        "-i", "--input", metavar="STRING", help="Input folder", required=False, dest="input", default="./data")
    parser.add_argument(
        "-o", "--output", metavar="STRING", help="Output report folder", required=False, dest="output", default="./report")
    parser.add_argument(
        "-a", "--address", metavar="STRING", help="Address to bind and serve the report", required=False, dest="address", default="localhost")
    parser.add_argument(
        "-p", "--port", metavar="STRING", help="Port to bind and serve the report", required=False, dest="port", default="8080")
    # Parse the arguments
    sys.exit(main(parser.parse_args()))
