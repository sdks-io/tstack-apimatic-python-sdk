from __future__ import annotations

from typing import TypeAlias

from .content31 import Content31, Content31Dict

Content21: TypeAlias = str | list[Content31]
"""Content of an assistant message. It can be a string or an array of text, image, reasoning, redacted reasoning, and
tool call parts."""

Content21Dict: TypeAlias = str | list[Content31Dict]
