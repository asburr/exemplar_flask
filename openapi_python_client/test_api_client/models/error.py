from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_errors import ErrorErrors


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        code (int | Unset): Error code
        message (str | Unset): Error message
        errors (ErrorErrors | Unset): Errors
        status (str | Unset): Error name
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    errors: ErrorErrors | Unset = UNSET
    status: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if errors is not UNSET:
            field_dict["errors"] = errors
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_errors import ErrorErrors

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: ErrorErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorErrors.from_dict(_errors)

        status = d.pop("status", UNSET)

        error = cls(
            code=code,
            message=message,
            errors=errors,
            status=status,
        )

        return error
