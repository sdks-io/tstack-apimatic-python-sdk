from __future__ import annotations

from typing import TypeAlias

from .image111 import Image111, Image111Dict

Image1: TypeAlias = Image111 | str
"""Image data. Can either be:

- data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
- URL: a URL that points to the image"""

Image1Dict: TypeAlias = Image111Dict | str
