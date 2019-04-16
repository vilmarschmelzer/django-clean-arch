from abc import ABC, abstractmethod

from project.libs.response import ItemResp, ItemsResp
from project.product.entities import Category

from .requests import (
    CreateCategoryRequest,
    DeleteCategoryRequest,
    FindCategoriesRequest,
    GetCategoryByIdRequest,
    UpdateCategoryRequest,
)


class ICategoryRepo(ABC):

    @abstractmethod
    def find(self, search: str) -> ItemsResp:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> ItemResp:
        raise NotImplementedError
    
    @abstractmethod
    def create(self, category: Category) -> ItemResp:
        raise NotImplementedError

    @abstractmethod
    def update(self, category: Category) -> ItemResp:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> ItemResp:
        raise NotImplementedError


class ICategoryUseCase(ABC):

    @abstractmethod
    def find(self, req: FindCategoriesRequest) -> ItemsResp:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, req: GetCategoryByIdRequest) -> ItemResp:
        raise NotImplementedError
    
    @abstractmethod
    def create(self, req: CreateCategoryRequest) -> ItemResp:
        raise NotImplementedError

    @abstractmethod
    def update(self, req: UpdateCategoryRequest) -> ItemResp:
        raise NotImplementedError

    @abstractmethod
    def delete(self, req: DeleteCategoryRequest) -> ItemResp:
        raise NotImplementedError
