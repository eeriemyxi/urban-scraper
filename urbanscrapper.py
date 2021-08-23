import aiohttp as http
from bs4 import BeautifulSoup as bs4
import requests
import urllib

class Definition():
    def __init__(self, dict: dict) -> dict:
        self.dict = dict
        self.word = dict['word']
        self.example = dict['example']
        self.meaning = dict['meaning']
        self.author = dict['author']
        self.date = dict['date']
        self.upvotes = dict['upvotes']
        self.downvotes = dict['downvotes']
        self.url = dict['url']
    def json(self):
        return self.dict

class Async:
    @classmethod
    async def define(self,keyword):
        async with http.ClientSession() as session:
            async with session.get((url := f'https://www.urbandictionary.com/define.php?term={keyword}')) as res:
                if res.status == 404: raise ValueError('No definitions found.')
                content = await res.text()
                soup = bs4(content, 'html.parser')
                divs = soup.find_all('div', attrs={'class': 'def-panel'})
                definitions = []

                for div in divs:
                    self.word = div.find(attrs={'class': 'word'}).text
                    if not self.word.lower().startswith(keyword.lower()): continue

                    self.meaning = div.find(attrs={'class': 'meaning'}).text

                    contributor = div.find(attrs={'class': 'contributor'})

                    self.date = " ".join(contributor.text.split(' ')[-3:])

                    self.author = contributor.find('a').text

                    self.example = div.find(attrs={'class': 'example'}).text
                    self.example = self.example.replace('\r', '\n') ; self.example = self.example.replace('/"', '"') ; self.example = self.example.replace('\t', '\n')


                    div_footer = div.find(attrs={'class': 'def-footer'})
                    thumbs = div_footer.find_all('span', attrs={'class': 'count'})

                    self.upvotes = int((votes := [i.text for i in thumbs])[0])

                    self.downvotes = int(votes[1])


                    definitions.append(Definition({
                        'meaning': self.meaning,
                        'author': self.author,
                        'date': self.date,
                        'word': self.word,
                        'example': self.example,
                        'upvotes': self.upvotes,
                        'downvotes': self.downvotes,
                        'url': urllib.parse.quote(url)
                    }))
                if len(definitions) > 0: return definitions 
                else: raise ValueError('No definition found.')
                    
                    
def define(keyword):
    res = requests.get((url := f'https://www.urbandictionary.com/define.php?term={keyword}'))
    if res.status_code == 404: raise ValueError('No definitions found.')
    soup = bs4(res.text, 'html.parser')
    divs = soup.find_all('div', attrs={'class': 'def-panel'})
    definitions = []
    
    for div in divs:
        word = div.find(attrs={'class': 'word'}).text
        if not word.lower().startswith(keyword.lower()): continue

        meaning = div.find(attrs={'class': 'meaning'}).text

        contributor = div.find(attrs={'class': 'contributor'})

        date = " ".join(contributor.text.split(' ')[-3:])

        author = contributor.find('a').text

        example = div.find(attrs={'class': 'example'}).text
        example = example.replace('\r', '\n') ; example = example.replace('/"', '"') ; example = example.replace('\t', '\n')

        div_footer = div.find(attrs={'class': 'def-footer'})
        thumbs = div_footer.find_all('span', attrs={'class': 'count'})

        upvotes = int((votes := [i.text for i in thumbs])[0])

        downvotes = int(votes[1])


        definitions.append(Definition({
            'meaning': meaning,
            'author': author,
            'date': date,
            'word': word,
            'example': example,
            'upvotes': upvotes,
            'downvotes': downvotes,
            'url': urllib.parse.quote(url)
        }))
    if len(definitions) > 0: return definitions