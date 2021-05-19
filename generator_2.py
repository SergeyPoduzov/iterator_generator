import requests
import hashlib

def download(url):
    response = requests.get(url)
    iter_content2 = response.iter_lines()
    for chunk in iter_content2:
        yield chunk

with open('hash2.txt', 'w', encoding='utf-8') as file:
    for chunk in download('https://raw.githubusercontent.com/mledoze/countries/master/countries.json'):
        hash_object = hashlib.md5(chunk)
        print(hash_object.hexdigest())
        file.write(hash_object.hexdigest())
