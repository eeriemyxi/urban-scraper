from re import I
import aiohttp as http
import asyncio
from bs4 import BeautifulSoup as bs4
import requests
from requests.models import codes
class Async:
    @classmethod
    async def define(self,keyword):
        async with http.ClientSession() as session:
            async with session.get(
                    f'https://www.urbandictionary.com/define.php?term={keyword}'
            ) as res:
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
                    if '\r' in self.example: self.example = self.example.replace('\r', '\n')

                    div_footer = div.find(attrs={'class': 'def-footer'})
                    thumbs = div_footer.find_all('span', attrs={'class': 'count'})

                    self.upvotes = int((votes := [i.text for i in thumbs])[0])

                    self.downvotes = int(votes[1])


                    definitions.append({
                        'meaning': self.meaning,
                        'author': self.author,
                        'date': self.date,
                        'word': self.word,
                        'example': self.example,
                        'upvotes': self.upvotes,
                        'downvotes': self.downvotes
                    })
                if len(definitions) > 0: return definitions 
                else: raise ValueError('No definition found.')
def define(keyword):
    res = requests.get(f'https://www.urbandictionary.com/define.php?term={keyword}')
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
        if '\r' in example: example = example.replace('\r', '\n')

        div_footer = div.find(attrs={'class': 'def-footer'})
        thumbs = div_footer.find_all('span',
                                        attrs={'class': 'count'})

        upvotes = int((votes := [i.text for i in thumbs])[0])

        downvotes = int(votes[1])


        definitions.append({
            'meaning': meaning,
            'author': author,
            'date': date,
            'word': word,
            'example': example,
            'upvotes': upvotes,
            'downvotes': downvotes
        })
    if len(definitions) > 0: return definitions