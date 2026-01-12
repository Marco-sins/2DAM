import urllib.request

url = "https://support.kaspersky.com/KWTS/6.1/es-ES/166244.html"

response = urllib.request.urlopen(url)

for _ in range(20):
    line = response.readline()
    print(line.decode('utf-8').strip())