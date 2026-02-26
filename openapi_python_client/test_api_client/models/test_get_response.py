from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestGetResponse")


@_attrs_define
class TestGetResponse:
    """
    Attributes:
        field1 (str):
        field2 (str):
        id (int | Unset):
    """

    field1: str
    field2: str
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field1 = self.field1

        field2 = self.field2

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field1": field1,
                "field2": field2,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field1 = d.pop("field1")

        field2 = d.pop("field2")

        id = d.pop("id", UNSET)

        test_get_response = cls(
            field1=field1,
            field2=field2,
            id=id,
        )

        return test_get_response
