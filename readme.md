## Asynchronous and synchronous [Urban dictionary](https://www.urbandictionary.com/)  scrapper for Python
### Asynchronous

```python
from urbanscrapper import Async
import asyncio

loop = asyncio.get_event_loop()

print(

loop.run_until_complete(Async.define("Hello world!"))

)
```
### Synchronous
```python
from urbanscrapper import define

print(

define("Hello world!"

)
```
### Error handling 
#####  if no definitions were found, it will raise [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) exception
