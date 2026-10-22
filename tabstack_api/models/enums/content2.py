from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Content2(str, Enum):
    """Content scope. "main" (default) returns the main article content; "full" returns the whole page, including
    navigation, footer, and links."""

    MAIN = "main"
    FULL = "full"

    __str__ = str.__str__


Content2OrStr: TypeAlias = Annotated[Content2 | str, open_enum_validator(Content2)]
