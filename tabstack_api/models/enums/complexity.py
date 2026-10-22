from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Complexity(str, Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"

    __str__ = str.__str__


ComplexityOrStr: TypeAlias = Annotated[Complexity | str, open_enum_validator(Complexity)]
