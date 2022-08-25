from . import errors as errors
from .admin import kill as kill, set_password as set_password
from .attribute_adapter import AttributeAdapter as AttributeAdapter
from .blob import MatCell as MatCell, MatStruct as MatStruct
from .connection import Connection as Connection, conn as conn
from .diagram import Diagram as Diagram
from .errors import DataJointError as DataJointError
from .expression import AndList as AndList, Not as Not, U as U
from .fetch import key as key
from .hash import key_hash as key_hash
from .schemas import (
    Schema as Schema,
    VirtualModule as VirtualModule,
    list_schemas as list_schemas,
)
from .settings import config as config
from .table import FreeTable as FreeTable, Table as Table
from .user_tables import (
    Computed as Computed,
    Imported as Imported,
    Lookup as Lookup,
    Manual as Manual,
    Part as Part,
)
from .version import __version__ as __version__

__author__: str
ERD = Diagram
Di = Diagram
schema = Schema
create_virtual_module = VirtualModule
