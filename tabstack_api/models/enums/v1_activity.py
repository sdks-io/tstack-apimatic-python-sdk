from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1Activity(str, Enum):
    """Activity types for research workflow"""

    PREFETCHING = "prefetching"
    PLANNING = "planning"
    ITERATION = "iteration"
    SEARCHING = "searching"
    ANALYZING = "analyzing"
    FOLLOWING = "following"
    EVALUATING = "evaluating"
    OUTLINING = "outlining"
    WRITING = "writing"
    JUDGING = "judging"

    __str__ = str.__str__


V1ActivityOrStr: TypeAlias = Annotated[V1Activity | str, open_enum_validator(V1Activity)]
