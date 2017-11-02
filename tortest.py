import requests

url="https://check.torproject.org/?lang=en_US"
proxy=dict(http='socks5://127.0.0.1:9150',
https='socks5://127.0.0.1:9150')
response = requests.get(url, proxies=proxy)
print(response.text)