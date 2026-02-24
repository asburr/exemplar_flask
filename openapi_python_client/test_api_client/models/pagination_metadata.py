from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationMetadata")


@_attrs_define
class PaginationMetadata:
    """
    Attributes:
        total (int | Unset):
        total_pages (int | Unset):
        first_page (int | Unset):
        last_page (int | Unset):
        page (int | Unset):
        previous_page (int | Unset):
        next_page (int | Unset):
    """

    total: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    first_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    page: int | Unset = UNSET
    previous_page: int | Unset = UNSET
    next_page: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        total_pages = self.total_pages

        first_page = self.first_page

        last_page = self.last_page

        page = self.page

        previous_page = self.previous_page

        next_page = self.next_page

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if first_page is not UNSET:
            field_dict["first_page"] = first_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if page is not UNSET:
            field_dict["page"] = page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        first_page = d.pop("first_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        page = d.pop("page", UNSET)

        previous_page = d.pop("previous_page", UNSET)

        next_page = d.pop("next_page", UNSET)

        pagination_metadata = cls(
            total=total,
            total_pages=total_pages,
            first_page=first_page,
            last_page=last_page,
            page=page,
            previous_page=previous_page,
            next_page=next_page,
        )

        return pagination_metadata
