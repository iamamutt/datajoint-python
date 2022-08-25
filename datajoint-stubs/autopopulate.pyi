from .errors import (
    DataJointError as DataJointError,
    LostConnectionError as LostConnectionError,
)
from .expression import AndList as AndList, QueryExpression as QueryExpression
from _typeshed import Incomplete

logger: Incomplete

def _initialize_populate(table, jobs, populate_kwargs) -> None: ...
def _call_populate1(key): ...

class AutoPopulate:
    _key_source: Incomplete
    _allow_insert: bool
    @property
    def key_source(self): ...
    def make(self, key) -> None: ...
    @property
    def target(self): ...
    def _job_key(self, key): ...
    def _jobs_to_do(self, restrictions): ...
    def populate(
        self,
        *restrictions,
        suppress_errors: bool = ...,
        return_exception_objects: bool = ...,
        reserve_jobs: bool = ...,
        order: str = ...,
        limit: Incomplete | None = ...,
        max_calls: Incomplete | None = ...,
        display_progress: bool = ...,
        processes: int = ...,
        make_kwargs: Incomplete | None = ...
    ): ...
    def _populate1(
        self,
        key,
        jobs,
        suppress_errors,
        return_exception_objects,
        make_kwargs: Incomplete | None = ...,
    ): ...
    def progress(self, *restrictions, display: bool = ...): ...
