
# Asynchronous and Synchronous Urban dictionary scraper

It uses [selectolax](https://github.com/rushter/selectolax) to parse the HTML and [httpx](https://github.com/encode/httpx) for sending HTTP requests.

## Asynchronous Example

```python
import asyncio
from urban_scraper import adefine


async def main():
    definitions = await adefine('hello')
    async for definition in definitions:
        ...

asyncio.run(main())
```

## Synchronous Example
```python
from urban_scraper import define

definitions = define('hello')

for definition in definitions:
    ...
```

**In both examples, `definition` is [`urban_scraper.Definition`](https://github.com/m-y-x-i/urban-scrapper/blob/36bb177a14e88ea843c7497feae672a980615b5e/urban_scraper/_dataclasses.py#L10-L25)**

## Attributes and Methods of [urban_scraper.Definition](https://github.com/m-y-x-i/urban-scrapper/blob/36bb177a14e88ea843c7497feae672a980615b5e/urban_scraper/_dataclasses.py#L10-L25)
Attributes
- `defid`
- `name`
- `meaning`
- `example`
- `author`
  - `name`
  - `url`
- `date`
- `upvote`
- `downvote`
Methods
- `as_dict()`
  - This will return a `dict` object of the Definition object.