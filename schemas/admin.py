"""Admin-side pydantic schemas"""

import datetime

from typing import TypeVar

from pydantic import BaseModel, Field, condecimal, validator

T = TypeVar("T", bound=str)


def must_not_digit(title: T) -> T:
    if title.isdigit():
        raise ValueError("Название не должно быть числом.")
    return title


class CategoryModel(BaseModel):
    """Category schema"""

    title: str = Field(max_length=50)
    photo: str = ''
    show: bool = True

    _must_not_digit_title = validator("title", allow_reuse=True, check_fields=False)(must_not_digit)


class SubCategoryModel(BaseModel):
    """SubCategory schema"""

    title: str = Field(max_length=50)
    photo: str = ''
    show: bool = True
    category_id: int

    _must_not_digit_title = validator("title", allow_reuse=True, check_fields=False)(must_not_digit)


class ItemModel(BaseModel):
    """Item schema"""

    name: str = Field(max_length=50)
    description: str = ""
    photo: str = ''
    price: condecimal(max_digits=12, decimal_places=2)
    subcategory_id: int
    show: bool = True
    files: list[str] = ''

    _must_not_digit_title = validator("title", allow_reuse=True, check_fields=False)(must_not_digit)
