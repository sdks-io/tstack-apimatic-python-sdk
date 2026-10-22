from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Relevance(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    __str__ = str.__str__


RelevanceOrStr: TypeAlias = Annotated[Relevance | str, open_enum_validator(Relevance)]
