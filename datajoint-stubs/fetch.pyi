from . import blob as blob, hash as hash
from .errors import DataJointError as DataJointError
from .settings import config as config
from .utils import safe_write as safe_write
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete

class key: ...

def is_key(attr): ...
def to_dicts(recarray) -> Generator[Incomplete, None, None]: ...
def _get(connection, attr, data, squeeze, download_path): ...
def _flatten_attribute_list(
    primary_key, attrs
) -> Generator[Incomplete, None, None]: ...

class Fetch:
    _expression: Incomplete
    def __init__(self, expression) -> None: ...
    def __call__(
        self,
        *attrs,
        offset: Incomplete | None = ...,
        limit: Incomplete | None = ...,
        order_by: Incomplete | None = ...,
        format: Incomplete | None = ...,
        as_dict: Incomplete | None = ...,
        squeeze: bool = ...,
        download_path: str = ...
    ): ...

class Fetch1:
    _expression: Incomplete
    def __init__(self, expression) -> None: ...
    def __call__(self, *attrs, squeeze: bool = ..., download_path: str = ...): ...
