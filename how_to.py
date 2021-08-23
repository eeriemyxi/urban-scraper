from urbanscrapper import Async, define

"""
    Asynchronous:
"""

import asyncio
loop = asyncio.get_event_loop()

definitions = loop.run_until_complete(Async.define('Hello world'))

"""
    Synchronous:
"""

definitions = define('Hello world')


#------------------
#| How to use it: |
#------------------

for definition in definitions:
    # This will return python dict object of the definition
    print(definition.json()) ; print('--------------------')
    # Methods:
    methods = [
        definition.word,
        definition.meaning,
        definition.date,
        definition.author,
        definition.url,
        definition.example,
        str(definition.upvotes),
        str(definition.downvotes),
    ]
    print("\n----------------\n".join(methods))
    break 