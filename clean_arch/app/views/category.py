
from django.db import transaction
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.libs.response import django_to_reponse
from project.product.category.requests import (
    CreateCategoryRequest,
    DeleteCategoryRequest,
    FindCategoriesRequest,
    GetCategoryByIdRequest,
    UpdateCategoryRequest,
)
from project.product.category.schemas import CategorySchema


class CategoryAPI(APIView):
    us = None

    def get(self, request, id=None):
        if id:
            resp = self.us.get_by_id(GetCategoryByIdRequest(id=id))
        else:
            resp = self.us.find(
                FindCategoriesRequest(
                    search=request.query_params.get("search")
                )
            )
        
        return django_to_reponse(resp, CategorySchema)

    @method_decorator(transaction.atomic)
    def post(self, request):
        resp = self.us.create(
            CreateCategoryRequest(name=request.data.get('name'))
        )

        return django_to_reponse(resp, CategorySchema)

    @method_decorator(transaction.atomic)
    def delete(self, request, id):
        resp = self.us.delete(DeleteCategoryRequest(id=id))

        return django_to_reponse(resp, CategorySchema)

    @method_decorator(transaction.atomic)
    def put(self, request, id):
        resp = self.us.update(
            UpdateCategoryRequest(id=id,
            name=request.data.get('name'))
        )

        return django_to_reponse(resp, CategorySchema)

