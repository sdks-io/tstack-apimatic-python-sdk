from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Coverage(str, Enum):
    LIGHT = "Light"
    MODERATE = "Moderate"
    SOLID = "Solid"
    COMPREHENSIVE = "Comprehensive"

    __str__ = str.__str__


CoverageOrStr: TypeAlias = Annotated[Coverage | str, open_enum_validator(Coverage)]
