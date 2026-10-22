from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1UrlSource(str, Enum):
    """URL source tracking - where a URL came from"""

    USER_INPUT = "user-input"
    SEARCH_RESULT = "search-result"
    EXTRACTED_LINK = "extracted-link"

    __str__ = str.__str__


V1UrlSourceOrStr: TypeAlias = Annotated[V1UrlSource | str, open_enum_validator(V1UrlSource)]
