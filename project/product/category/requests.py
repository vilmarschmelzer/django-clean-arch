from project.libs.dataclasses import dataclass


@dataclass
class GetCategoryByIdRequest:
    id: int = None


@dataclass
class FindCategoriesRequest:
    search: str = None


@dataclass
class CreateCategoryRequest:
    name: str = None


@dataclass
class UpdateCategoryRequest:
    id: int = None
    name: str = None


@dataclass
class DeleteCategoryRequest:
    id: int = None