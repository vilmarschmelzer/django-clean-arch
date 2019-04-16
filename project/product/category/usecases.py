from project.libs.response import ItemResp, ItemsResp
from project.libs.validators.request import validate_request
from project.product.entities import Category

from . import schemas
from .interfaces import ICategoryRepo, ICategoryUseCase
from .requests import (
    CreateCategoryRequest,
    DeleteCategoryRequest,
    FindCategoriesRequest,
    GetCategoryByIdRequest,
    UpdateCategoryRequest,
)


class CategoryUseCase(ICategoryUseCase):
    def __init__(self, repo: ICategoryRepo):
        self.repo = repo

    @validate_request(schema=schemas.FindCategoriesSchema)
    def find(self, req: FindCategoriesRequest) -> ItemsResp:
        return self.repo.find(req.search)

    @validate_request(schema=schemas.CreateCategorySchema)
    def create(self, req: CreateCategoryRequest):

        category = Category(
            name=req.name,
        )

        return self.repo.create(category)

    @validate_request(schema=schemas.UpdateCategorySchema)
    def update(self, req: UpdateCategoryRequest) -> ItemResp:

        resp = self.repo.get_by_id(
            id=req.id,
        )
        if not resp.ok:
            return resp

        category = resp.item
        category.name = req.name

        return self.repo.update(category)

    @validate_request(schema=schemas.GetCategoryByIdSchema)
    def get_by_id(self, req: GetCategoryByIdRequest) -> ItemResp:
        return self.repo.get_by_id(req.id)
    
    @validate_request(schema=schemas.GetCategoryByIdSchema)
    def delete(self, req: DeleteCategoryRequest) -> ItemResp:
        return self.repo.get_by_id(req.id)
