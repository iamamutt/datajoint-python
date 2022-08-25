from .connection import conn as conn
from .settings import config as config
from .utils import user_choice as user_choice
from _typeshed import Incomplete

def set_password(
    new_password: Incomplete | None = ...,
    connection: Incomplete | None = ...,
    update_config: Incomplete | None = ...,
) -> None: ...
def kill(
    restriction: Incomplete | None = ...,
    connection: Incomplete | None = ...,
    order_by: Incomplete | None = ...,
) -> None: ...
def kill_quick(
    restriction: Incomplete | None = ..., connection: Incomplete | None = ...
): ...
