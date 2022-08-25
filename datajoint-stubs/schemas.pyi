import types
from .connection import conn as conn
from .diagram import Diagram as Diagram, _get_tier as _get_tier
from .errors import AccessError as AccessError, DataJointError as DataJointError
from .external import ExternalMapping as ExternalMapping
from .heading import Heading as Heading
from .jobs import JobTable as JobTable
from .settings import config as config
from .table import (
    FreeTable as FreeTable,
    Log as Log,
    lookup_class_name as lookup_class_name,
)
from .user_tables import (
    Computed as Computed,
    Imported as Imported,
    Lookup as Lookup,
    Manual as Manual,
    Part as Part,
)
from .utils import to_camel_case as to_camel_case, user_choice as user_choice
from _typeshed import Incomplete

logger: Incomplete

def ordered_dir(class_): ...

class Schema:
    _log: Incomplete
    connection: Incomplete
    database: Incomplete
    context: Incomplete
    create_schema: Incomplete
    create_tables: Incomplete
    _jobs: Incomplete
    external: Incomplete
    add_objects: Incomplete
    declare_list: Incomplete
    def __init__(
        self,
        schema_name: Incomplete | None = ...,
        context: Incomplete | None = ...,
        *,
        connection: Incomplete | None = ...,
        create_schema: bool = ...,
        create_tables: bool = ...,
        add_objects: Incomplete | None = ...
    ) -> None: ...
    def is_activated(self): ...
    def activate(
        self,
        schema_name: Incomplete | None = ...,
        *,
        connection: Incomplete | None = ...,
        create_schema: Incomplete | None = ...,
        create_tables: Incomplete | None = ...,
        add_objects: Incomplete | None = ...
    ) -> None: ...
    def _assert_exists(self, message: Incomplete | None = ...) -> None: ...
    def __call__(self, cls, *, context: Incomplete | None = ...): ...
    def _decorate_master(self, cls, context) -> None: ...
    def _decorate_table(
        self, table_class, context, assert_declared: bool = ...
    ) -> None: ...
    @property
    def log(self): ...
    def __repr__(self): ...
    @property
    def size_on_disk(self): ...
    def spawn_missing_classes(self, context: Incomplete | None = ...) -> None: ...
    def drop(self, force: bool = ...) -> None: ...
    @property
    def exists(self): ...
    @property
    def jobs(self): ...
    @property
    def code(self): ...
    def save(self, python_filename: Incomplete | None = ...): ...
    def list_tables(self): ...

class VirtualModule(types.ModuleType):
    def __init__(
        self,
        module_name,
        schema_name,
        *,
        create_schema: bool = ...,
        create_tables: bool = ...,
        connection: Incomplete | None = ...,
        add_objects: Incomplete | None = ...
    ) -> None: ...

def list_schemas(connection: Incomplete | None = ...): ...
