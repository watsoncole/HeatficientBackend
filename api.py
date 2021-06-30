import json
import time
import urllib.request
import time

from http.server import BaseHTTPRequestHandler, HTTPServer
from config import API_KEY

LOCATION_ID = 337219
hostName = "localhost"
serverPort = 8080


hostName = "localhost"
serverPort = 8080

def get_weather(api, loc):
    url = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/%s.json?apikey=%s' % (loc, api)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())


    temperatures = ""
    for i in range(0,11):
	    temperatures += str(data[i]['Temperature']['Value']) + ", "
    return temperatures

temps = get_weather(API_KEY,LOCATION_ID)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>%s</p>"%(temps), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

def main():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    #print(time.time())
    try:
            webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()

main()
