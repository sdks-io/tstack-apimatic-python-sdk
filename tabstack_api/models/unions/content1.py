from __future__ import annotations

from typing import TypeAlias

from ..file import File, FileDict
from ..image import Image, ImageDict
from ..text import Text, TextDict

Content1: TypeAlias = Text | Image | File

Content1Dict: TypeAlias = TextDict | ImageDict | FileDict
