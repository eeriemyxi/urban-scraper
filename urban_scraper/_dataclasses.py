from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Author:
    name: str
    url: str


@dataclass(init=True)
class Definition:
    defid: int
    name: str
    meaning: str
    example: str
    author: Author
    date: datetime
    upvote: int = None
    downvote: int = None

    def as_dict(self):
        '''
        Converts the dataclass to a `dict` object and returns it.
        '''
        return asdict(self)
