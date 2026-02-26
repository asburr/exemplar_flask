from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Test2PostRequestJson")


@_attrs_define
class Test2PostRequestJson:
    """
    Attributes:
        field3 (str):
    """

    field3: str

    def to_dict(self) -> dict[str, Any]:
        field3 = self.field3

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field3": field3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field3 = d.pop("field3")

        test_2_post_request_json = cls(
            field3=field3,
        )

        return test_2_post_request_json
