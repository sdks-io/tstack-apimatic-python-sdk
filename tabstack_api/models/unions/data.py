from __future__ import annotations

from typing import TypeAlias

from .data11 import Data11, Data11Dict

Data: TypeAlias = Data11 | str
"""File data. Can either be:

- data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
- URL: a URL that points to the image"""

DataDict: TypeAlias = Data11Dict | str
