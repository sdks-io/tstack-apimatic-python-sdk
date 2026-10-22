from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reliability(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    __str__ = str.__str__


ReliabilityOrStr: TypeAlias = Annotated[Reliability | str, open_enum_validator(Reliability)]
