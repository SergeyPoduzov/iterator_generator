import requests
import hashlib

class Downloader:

    def __init__(self,url):
        self.url = url
        response = requests.get(url)

        self.iter_content2 = response.iter_lines()


    def __iter__(self):
        return self

    def __next__(self):

        chunk = next(self.iter_content2)
        # Предположительно по умолчанию UTF-8
        hash_object = hashlib.md5(chunk)
        # при каждой итерации возвращает md5 хеш каждой строки файла.
        print(hash_object.hexdigest())

        return hash_object

    def download(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for chunk2 in self:
                file.write(chunk2.hexdigest())


downloader = Downloader('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')

downloader.download('hash1.txt')
