from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Test2GetResponse")


@_attrs_define
class Test2GetResponse:
    """
    Attributes:
        test_id (str):
        field2 (str):
        field3 (str):
        id (int | Unset):
    """

    test_id: str
    field2: str
    field3: str
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        test_id = self.test_id

        field2 = self.field2

        field3 = self.field3

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "test_id": test_id,
                "field2": field2,
                "field3": field3,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_id = d.pop("test_id")

        field2 = d.pop("field2")

        field3 = d.pop("field3")

        id = d.pop("id", UNSET)

        test_2_get_response = cls(
            test_id=test_id,
            field2=field2,
            field3=field3,
            id=id,
        )

        return test_2_get_response
