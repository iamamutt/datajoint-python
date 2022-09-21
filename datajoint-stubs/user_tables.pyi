from typing import ClassVar

from _typeshed import Incomplete

from .autopopulate import AutoPopulate as AutoPopulate
from .errors import DataJointError as DataJointError
from .table import Table as Table
from .utils import ClassProperty as ClassProperty
from .utils import from_camel_case as from_camel_case

_base_regexp: str
supported_class_attrs: Incomplete

class TableMeta(type):
    def __getattribute__(cls, name): ...
    def __and__(cls, arg): ...
    def __xor__(cls, arg): ...
    def __sub__(cls, arg): ...
    def __neg__(cls): ...
    def __mul__(cls, arg): ...
    def __matmul__(cls, arg): ...
    def __add__(cls, arg): ...
    def __iter__(cls): ...

class UserTable(Table, metaclass=TableMeta):
    _connection: Incomplete
    _heading: Incomplete
    _support: Incomplete
    tier_regexp: Incomplete
    _prefix: Incomplete

    definition: ClassVar[str]

    def connection(cls): ...
    def table_name(cls): ...
    def full_table_name(cls): ...

class Manual(UserTable):
    _prefix: str
    tier_regexp: Incomplete

class Lookup(UserTable):
    _prefix: str
    tier_regexp: Incomplete

class Imported(UserTable, AutoPopulate):
    _prefix: str
    tier_regexp: Incomplete

class Computed(UserTable, AutoPopulate):
    _prefix: str
    tier_regexp: Incomplete

class Part(UserTable):
    _connection: Incomplete
    _master: Incomplete
    tier_regexp: Incomplete
    def connection(cls): ...
    def full_table_name(cls): ...
    def master(cls): ...
    def table_name(cls): ...
    def delete(self, force: bool = ...) -> None: ...
    def drop(self, force: bool = ...) -> None: ...
