from typing import Literal, TypeVar, Tuple, Union


T = TypeVar("T")
ColorType = Tuple[int, int, int, int]
AnchorType = Union[int, Literal["top", "bottom", "center", "baseline"]]
