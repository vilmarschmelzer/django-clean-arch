from clean_arch.app.models import Category as DjCategory
from project.libs.response import ItemResp, ItemsResp, Status
from project.product.entities import Category

from .interfaces import ICategoryRepo


class DjCategoryRepo(ICategoryRepo):

    def find(self, search) -> ItemsResp:
        dj_categories = DjCategory.objects.filter(
            name__icontains=search
        )

        categories = []
        for dj_category in dj_categories:
            categories.append(
                django_to_category(dj_category)
            )

        return ItemResp(items=categories)

    def get_by_id(self, id: int):
        try:
            dj_category = DjCategory.objects.get(
                id=id
            )
        except DjCategory.DoesNotExist:
            return ItemResp(status=Status.not_found)

        return ItemResp(
            item=django_to_category(dj_category)
        )

    def create(self, category):
        dj_category = category_to_django(
            category
        )
        dj_category.save()
        category.id = dj_category.id
        return ItemResp(item=category)

    def update(self, category):
        dj_category = category_to_django(
            category
        )
        dj_category.save()
        category.id = dj_category.id
        return ItemResp(item=category)


def django_to_category(
    dj_category: DjCategory,
) -> Category:
    return Category(
        id=dj_category.id,
        name=dj_category.name,
    )


def category_to_django(category: Category):
    return DjCategory(
        id=category.id,
        name=category.name,
    )
