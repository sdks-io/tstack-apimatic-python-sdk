from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Effort(str, Enum):
    """Fetch effort level controlling speed vs. capability tradeoff. "min": fastest, no fallback (1-5s). "standard":
    balanced with enhanced reliability (default, 3-15s). "max": full browser rendering for JS-heavy sites (15-60s)."""

    MIN = "min"
    STANDARD = "standard"
    MAX = "max"

    __str__ = str.__str__


EffortOrStr: TypeAlias = Annotated[Effort | str, open_enum_validator(Effort)]
