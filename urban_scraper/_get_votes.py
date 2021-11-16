from collections import UserDict

import httpx
from yarl import URL

API_URL = URL("https://api.urbandictionary.com/v0/uncacheable")


class CustomDict(UserDict):
    def __getattr__(self, attr):
        if attr in self.data:
            return self.data.get(attr)


def _sync_get_votes(ids: list):
    url = API_URL.with_query(ids=",".join(map(str, ids)))
    res = httpx.get(url.human_repr())
    return [CustomDict(i) for i in res.json().get('thumbs')]

async def _async_get_votes(ids: list):
    url = API_URL.with_query(ids=",".join(map(str, ids)))
    async with httpx.AsyncClient() as client:
        res = await client.get(url.human_repr())
        return [CustomDict(i) for i in res.json().get('thumbs')]

def _search_defid(id: int, votes: list[CustomDict]):
    for d in votes:
        if int(d.defid) == id:
            return d
    raise KeyError