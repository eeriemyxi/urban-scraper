from urbanscrapper import Async, define

"""
    Asynchronous:
"""

import asyncio
loop = asyncio.get_event_loop()
print(
    loop.run_until_complete(Async.define('Hello world'))
)

"""
    Synchronous:
"""

print(
    define('Hello world')
)