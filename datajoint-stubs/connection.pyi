from . import errors as errors
from .blob import pack as pack, unpack as unpack
from .dependencies import Dependencies as Dependencies
from .hash import uuid_from_buffer as uuid_from_buffer
from .plugin import connection_plugins as connection_plugins
from .settings import config as config
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
query_log_max_length: int
cache_key: str

def get_host_hook(host_input): ...
def connect_host_hook(connection_obj) -> None: ...
def translate_query_error(client_error, query): ...
def conn(
    host: Incomplete | None = ...,
    user: Incomplete | None = ...,
    password: Incomplete | None = ...,
    *,
    init_fun: Incomplete | None = ...,
    reset: bool = ...,
    use_tls: Incomplete | None = ...
): ...

class EmulatedCursor:
    _data: Incomplete
    _iter: Incomplete
    def __init__(self, data) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def fetchall(self): ...
    def fetchone(self): ...
    @property
    def rowcount(self): ...

class Connection:
    conn_info: Incomplete
    init_fun: Incomplete
    _conn: Incomplete
    _query_cache: Incomplete
    connection_id: Incomplete
    _in_transaction: bool
    schemas: Incomplete
    dependencies: Incomplete
    def __init__(
        self,
        host,
        user,
        password,
        port: Incomplete | None = ...,
        init_fun: Incomplete | None = ...,
        use_tls: Incomplete | None = ...,
    ) -> None: ...
    def __eq__(self, other): ...
    def __repr__(self): ...
    def connect(self) -> None: ...
    def set_query_cache(self, query_cache: Incomplete | None = ...) -> None: ...
    def purge_query_cache(self) -> None: ...
    def close(self) -> None: ...
    def register(self, schema) -> None: ...
    def ping(self) -> None: ...
    @property
    def is_connected(self): ...
    @staticmethod
    def _execute_query(cursor, query, args, suppress_warnings) -> None: ...
    def query(
        self,
        query,
        args=...,
        *,
        as_dict: bool = ...,
        suppress_warnings: bool = ...,
        reconnect: Incomplete | None = ...
    ): ...
    def get_user(self): ...
    @property
    def in_transaction(self): ...
    def start_transaction(self) -> None: ...
    def cancel_transaction(self) -> None: ...
    def commit_transaction(self) -> None: ...
    @property
    def transaction(self) -> Generator[Incomplete, None, None]: ...
