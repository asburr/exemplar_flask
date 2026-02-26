from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TestPostRequestJson")


@_attrs_define
class TestPostRequestJson:
    """
    Attributes:
        field2 (str):
    """

    field2: str

    def to_dict(self) -> dict[str, Any]:
        field2 = self.field2

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field2": field2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field2 = d.pop("field2")

        test_post_request_json = cls(
            field2=field2,
        )

        return test_post_request_json
