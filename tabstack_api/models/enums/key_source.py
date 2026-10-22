from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class KeySource(str, Enum):
    GLOBAL = "global"
    ENV = "env"
    NOT_SET = "not_set"

    __str__ = str.__str__


KeySourceOrStr: TypeAlias = Annotated[KeySource | str, open_enum_validator(KeySource)]
