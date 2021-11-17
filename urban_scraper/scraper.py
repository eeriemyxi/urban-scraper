import pathlib
import time
from datetime import datetime
from typing import Iterator

import httpx
import pickledb
from selectolax.parser import HTMLParser
from yarl import URL

from ._dataclasses import Author, Definition
from ._get_votes import _search_defid, _sync_get_votes
from ._months import MONTHS


def define(query: str) -> Iterator[Definition]:
    """Returns an iterator of all the `Definition` it could fetch."""
    gen = Define(query)
    return gen

class Caching:
    def __init__(self) -> None:
        self._ensure()

    def _ensure(self):
        path = pathlib.Path("_cache")
        if not path.exists():
            path.mkdir()
        self.pickle = pickledb.load(str(path.joinpath("cache.db")), True)

    def _get_html_cache(self):
        html = self.pickle.get(self.query.lower())
        if html is not False:
            if round(time.time() - html.get("time")) < 3600:
                return html.get("data")
            else:
                return None


class Define(Caching):
    def __init__(self, query: str):
        self.query = query.strip()
        self.url = URL("https://www.urbandictionary.com/define.php")
        self.query_url = self.url.with_query(term=self.query)
        super().__init__()
        self.iterator = self._iterdefs()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def _fetch_html(self):
        res = httpx.get(str(self.query_url))
        return res.text

    def _get_html(self):
        cache = self._get_html_cache()
        if cache:
            return cache
        else:
            html = self._fetch_html()
            cache_time = time.time()
            obj = dict(data=html, time=cache_time)
            self.pickle.set(self.query.lower(), obj)
            return html

    def _iterdefs(self):
        html = self._get_html()
        parser = HTMLParser(html, True)
        nodes = parser.css(".def-panel")
        defids = [int(i.attrs.get('data-defid')) for i in nodes]
        votes = _sync_get_votes(defids)
        for index, node in enumerate(nodes):
            contributor = node.css_first(".contributor")
            author = contributor.css_first("a")
            date = [i.strip(",") for i in contributor.text().split()[-3:]]

            defid = defids[index]
            name = node.css_first(".word").text()
            meaning = node.css_first(".meaning").text()
            example = node.css_first(".example").text()
            author_name = author.text()
            author_url = str(
                URL("https://www.urbandictionary.com").join(URL(author.attrs["href"]))
            )
            _datetime = datetime(
                year=int(date[2]), month=MONTHS.get(date[0]), day=int(date[1])
            )
            upvote = _search_defid(defid, votes).up
            downvote = _search_defid(defid, votes).down
            yield Definition(
                defid=defid,
                name=name,
                meaning=meaning,
                example=example,
                author=Author(name=author_name, url=author_url),
                date=_datetime,
                upvote=upvote,
                downvote=downvote
            )
