from .rest import REST
from .engines import Engine
from .collections import Collection
from .documents import Document

class Client(object):

    """Tinysou Client"""

    def __init__(self, token):
        self.token = token
        self.rest = REST(token)
        self.engines = Engine(self.rest)
        self.collections = Collection(self.rest)
        self.documents = Document(self.rest)
