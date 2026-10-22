from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1Mode(str, Enum):
    """Research mode determines depth, thinking budget, and quality controls

    Modes (in order of cost/thoroughness):
    - **fast**: Quick answers with minimal validation (~$2, 1 iteration, no judge)
    - **balanced**: Standard research with moderate depth (~$8, 3 iterations, Flash models, no judge)
    - **deep**: Thorough research with judge review (~$15, 5 iterations, Flash models, with judge)
    - **max**: Maximum quality with Pro models (~$40, 5 iterations, Pro models, with judge)
    - **ultra**: Ultimate tier - all Pro models, 10 iterations (expensive, for when accuracy is paramount)"""

    FAST = "fast"
    BALANCED = "balanced"
    DEEP = "deep"
    MAX = "max"
    ULTRA = "ultra"

    __str__ = str.__str__


V1ModeOrStr: TypeAlias = Annotated[V1Mode | str, open_enum_validator(V1Mode)]
