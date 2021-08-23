
##  Asynchronous and synchronous [Urban dictionary](https://www.urbandictionary.com/) scrapper for Python

###  Asynchronous

  

```python
from urbanscrapper import Async
import asyncio


loop = asyncio.get_event_loop()

loop.run_until_complete(Async.define("Hello world!"))
```

###  Synchronous

```python
from urbanscrapper import define

define("Hello world!")
```

**Check [`how_to.py`](https://github.com/m-y-x-i/urban-scrapper/blob/main/how_to.py) for more information**
###  Error handling

If no definitions were found, it will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) exception

###  Return value

It returns a list of [`urbanscrapper.Definition`](https://github.com/m-y-x-i/urban-scrapper/blob/f43a1ae3bb5d3d7a7c17af3fcb67450e90fa9310/urbanscrapper.py#L6-L18) objects. These are the methods and attributes of it:
#### Methods

 - `json()`
 it returns a Python dictionary object of the definition.

#### Attributes

 - `meaning`
 - `author`
 - `date`
 - `word`
 - `url`
 - `upvotes`
 - `downvotes`
 - `example`