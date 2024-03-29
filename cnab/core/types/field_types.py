from typing import TypedDict, TypeVar

DictField = TypedDict("DictField", {"value": str, "strict": bool})

TypesField = TypeVar("TypesField", str, DictField)
