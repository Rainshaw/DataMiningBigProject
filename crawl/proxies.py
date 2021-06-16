import random
from urllib.parse import quote
import requests
import time

server = ["🇭🇰 [CT/CM] HKBN A", "🇭🇰 [CT/CM] HKBN B", "🇭🇰 [CT/CM] HKBN C", "🇭🇰 [CT/CM] HKBN D", "🇭🇰 [CT/CM] HKBN E"]

while True:
    index = random.randint(0, len(server)-1)
    print(index)
    # res = requests.get(f'http://127.0.0.1:9090/proxies/{quote(server[index])}/delay?timeout=5000&url=http:%2F%2Fwww.gstatic.com%2Fgenerate_204')
    # print(quote(server[index]))
    res = requests.put('http://127.0.0.1:9090/proxies/GLOBAL', data=f"{{\"name\":\"{server[index]}\"}}".encode('utf-8'))
    print(res.status_code)
    time.sleep(290)
