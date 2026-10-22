from __future__ import annotations

from typing import TypeAlias

from ..data1 import Data1, Data1Dict
from ..v1_global_buffer import V1GlobalBuffer, V1GlobalBufferDict

Data11: TypeAlias = str | V1GlobalBuffer | Data1 | V1GlobalBuffer
"""Data content. Can either be a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer."""

Data11Dict: TypeAlias = str | V1GlobalBufferDict | Data1Dict | V1GlobalBufferDict
