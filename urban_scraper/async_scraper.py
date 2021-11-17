import json
import time
from datetime import datetime
from typing import AsyncIterator, Awaitable

import aiofiles
import aiopath
import httpx
from selectolax.parser import HTMLParser
from yarl import URL

from urban_scraper._dataclasses import Author, Definition
from urban_scraper._months import MONTHS

from ._get_votes import _async_get_votes, _search_defid


def anext(async_iterator: AsyncIterator) -> Awaitable:
    return async_iterator.__anext__()


async def define(query: str) -> AsyncIterator[Definition]:
    """Returns an async iterator of all the `Definition` it could fetch."""

    gen = await Define.construct(query)
    return gen


class Define:
    @classmethod
    async def construct(cls, query: str):
        self = Define()
        self.query = query.strip()
        self.url = URL("https://www.urbandictionary.com/define.php")
        self.query_url = self.url.with_query(term=self.query)
        await self._ensure()
        return self

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await anext(self.iterator)

    async def _ensure(self):
        path = aiopath.AsyncPath(__file__).parent.joinpath('_cache')
        if not await path.exists():
            await path.mkdir()
        self.path = path.joinpath("cache.db")
        if not await self.path.exists():
            async with aiofiles.open(self.path, "w") as cache_file:
                await cache_file.write("{}")
                await cache_file.close()
        self.iterator = self._iterdefs()

    async def _get_cache(self, key: str):
        async with aiofiles.open(self.path, "r") as cache_file:
            obj = json.loads(await cache_file.read())
            self.obj = obj
            if key.lower() in obj:
                return obj.get(key.lower())
            else:
                return None

    async def _get_html(self):
        html = await self._get_cache(self.query.lower())
        if html:
            if round(time.time() - html.get("time")) < 3600:
                return html.get("data")
        else:
            async with aiofiles.open(self.path, "w") as cache_file:
                html = await self._fetch_html()
                cache_time = time.time()
                self.obj[self.query.lower()] = dict(data=html, time=cache_time)
                await cache_file.write(json.dumps(self.obj))
                await cache_file.close()
            return html

    async def _fetch_html(self):
        async with httpx.AsyncClient() as client:
            res = await client.get(str(self.query_url))
            return res.text

    async def _iterdefs(self):
        html = await self._get_html()
        parser = HTMLParser(html, True)
        nodes = parser.css(".def-panel")
        defids = [int(i.attrs.get("data-defid")) for i in nodes]
        votes = await _async_get_votes(defids)
        for index, node in enumerate(parser.css(".def-panel")):
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
                downvote=downvote,
            )
