import requests

class Downloader:

    def __init__(self):
        pass


    def __iter__(self):
        return self

    def __next__(self):

        if self.start < self.end:
            self.start += 1
            self.content = self.res[self.start]
            self.txt = ''
            self.txt += self.content['name']['common']

            self.txt += ' - '
            try:
                self.txt += self.content['tld'][0]
            except:
                self.txt += 'none'
            self.txt +='\n'
            return self.txt


        else:
            self.start = -1
            raise StopIteration

    def download(self, url, file_path):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Wrong status code")
        self.res = response.json()
        self.start = -1
        self.end = len(self.res) - 1
        with open(file_path, 'w', encoding='utf-8') as file:
            for chunk in self:
                file.write(chunk)

    def printing(self):
        print("Все страны из класса: ")
        for chunk in self:
            print(chunk)

downloader = Downloader()

downloader.download('https://raw.githubusercontent.com/mledoze/countries/master/countries.json', 'count2.txt')
downloader.printing()