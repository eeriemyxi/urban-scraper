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
### Return value
#####  it returns Python dictionary object. `define("Hello world!"` would return something like this:
```json
[
    {
        meaning: "The easiest, and first program any newbie would write. Applies for any language. Also what you would see in the first chapter of most programming books. ",
        author: "The Black Jack",
        date: "October 26, 2006",
        word: "hello world",
        example: 'programming noob: Hey I just attended my first programming lesson earlier! \n.NET Veteran: Oh? What can you do?\nprogramming noob: I could make a dialog box pop up which says "Hello World!" !!!\n.NET Veteran: lmao.. hey guys! look.. check out this "hello world" programmer\n Console.WriteLine("Hello World")',
        upvotes: 164,
        downvotes: 53,
    },
    {
        meaning: "A common program written to demostrate the syntax of a programming language.",
        author: "peterson",
        date: "June 18, 2004",
        word: "Hello World",
        example: 'Hello World In Java!\nclass HelloWorld()\n{\npublic static void main(String  args)\n\t{\n\tSystem.out.println("Hello world");\n\t}\n}',
        upvotes: 54,
        downvotes: 37,
    },
    {
        meaning: "A typical sample programming application that once written, demonstrates complete mastery of choice language, particularly in subclassing and, of course, database API's.",
        author: "3",
        date: "January 23, 2004",
        word: "hello world",
        example: 'Dude, I spent 6 months developing this AI-based 3-tier search engine for this meeting, and Jon shows up with another great "Hello World" program and blows my ass away.  Again.',
        upvotes: 42,
        downvotes: 39,
    },
    {
        meaning: "First phrase we learn in CS 101 to print in a computer software program.",
        author: "buritob",
        date: "January 16, 2011",
        word: "hello world",
        example: 'She just created her first "hello world" program.',
        upvotes: 11,
        downvotes: 8,
    },
    {
        meaning: "First program a programmer normally writes.",
        author: "Eric's Mom's Lover",
        date: "June 18, 2004",
        word: "Hello World",
        example: '#include <stdio.h>\n int main()\n{\nprintf("Hello World\\n");\n return 0;\n}',
        upvotes: 26,
        downvotes: 31,
    },
    {
        meaning: 'Computer Programming: The first program that a programmer writes in a language he is learning. Typically, the program simply opens a window that says "Hello World." The simplicity of the program makes it ideal for use as a comparison between different programming languages.',
        author: "Kluekozyte",
        date: "January 22, 2004",
        word: "hello world",
        example: 'As a first step in learning Perl, create a "Hello World" application.',
        upvotes: 17,
        downvotes: 33,
    },
]
```
### Note
#### Try not to use the examples. In some cases, it looks weird. I'm working on it.
