from typing import List, Tuple, Any, Iterator

from ..base import *
from ..document import BaseDocument


class BaseIndexer(TrainableBase):
    def add(self, *args, **kwargs): pass

    def query(self, *args, **kwargs) -> List[List[Tuple[Any, float]]]: pass

    def close(self):
        super().close()


class BaseBinaryIndexer(BaseIndexer):
    def __init__(self):
        super().__init__()

    def add(self, vectors: bytes, doc_ids: bytes):
        pass

    def query(self, keys: bytes, top_k: int) -> List[List[Tuple[int, float]]]:
        pass


class BaseTextIndexer(BaseIndexer):
    def add(self, docs: Iterator[BaseDocument]): pass

    def query(self, keys: List[int]) -> List[Any]: pass
