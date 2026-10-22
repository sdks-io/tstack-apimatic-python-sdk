from __future__ import annotations

from typing import TypeAlias

from ..custom import Custom, CustomDict
from ..file_data import FileData, FileDataDict
from ..file_id import FileId, FileIdDict
from ..file_url import FileUrl, FileUrlDict
from ..image_data import ImageData, ImageDataDict
from ..image_file_id import ImageFileId, ImageFileIdDict
from ..image_url import ImageUrl, ImageUrlDict
from ..media import Media, MediaDict
from ..text3 import Text3, Text3Dict

Value4: TypeAlias = Text3 | Media | FileData | FileUrl | FileId | ImageData | ImageUrl | ImageFileId | Custom

Value4Dict: TypeAlias = (
    Text3Dict
    | MediaDict
    | FileDataDict
    | FileUrlDict
    | FileIdDict
    | ImageDataDict
    | ImageUrlDict
    | ImageFileIdDict
    | CustomDict
)
