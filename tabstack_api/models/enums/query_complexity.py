from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QueryComplexity(str, Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"

    __str__ = str.__str__


QueryComplexityOrStr: TypeAlias = Annotated[QueryComplexity | str, open_enum_validator(QueryComplexity)]
