import networkx as nx
from .errors import DataJointError as DataJointError
from _typeshed import Incomplete

def unite_master_parts(lst): ...

class Dependencies(nx.DiGraph):
    _conn: Incomplete
    _node_alias_count: Incomplete
    _loaded: bool
    def __init__(self, connection: Incomplete | None = ...) -> None: ...
    def clear(self) -> None: ...
    def load(self, force: bool = ...): ...
    def parents(self, table_name, primary: Incomplete | None = ...): ...
    def children(self, table_name, primary: Incomplete | None = ...): ...
    def descendants(self, full_table_name): ...
    def ancestors(self, full_table_name): ...