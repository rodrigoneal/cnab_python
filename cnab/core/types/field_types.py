from typing import TypeVar, TypedDict


DictField = TypedDict("DictField", {"value": str, "strict": bool})

TypesField = TypeVar("TypesField", str, DictField)
