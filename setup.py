from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="urban_scraper",
    version="1.1",
    packages=find_packages(include=["urban_scraper", "urban_scraper.*"]),
    install_requires=["aiofiles", "aiopath", "pickledb", "selectolax", "yarl", "httpx"],
    author="Myxi",
    author_email="myxi@duck.com",
    url="https://github.com/m-y-x-i/urban-scraper",
    description="Easy to use Urban Dictionary asynchronous and synchronous scraper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    license="GNU GPLv3",
)
