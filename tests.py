from urban_scraper import adefine
import asyncio

async def main():
    definitions = await adefine('hello')
    async for definition in definitions:
        print(definition)

asyncio.run(main())

# from urban_scraper import define

# definitions = define('hello')

# for definition in definitions:
#     print(definition)
#     print()
#     print()