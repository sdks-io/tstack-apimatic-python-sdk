from __future__ import annotations

from typing import TypeAlias

from ..image11 import Image11, Image11Dict
from ..v1_global_buffer import V1GlobalBuffer, V1GlobalBufferDict

Image111: TypeAlias = str | V1GlobalBuffer | Image11 | V1GlobalBuffer
"""Data content. Can either be a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer."""

Image111Dict: TypeAlias = str | V1GlobalBufferDict | Image11Dict | V1GlobalBufferDict
