from rest_framework import serializers

from .requests import (
    CreateCategoryRequest,
    DeleteCategoryRequest,
    FindCategoriesRequest,
    GetCategoryByIdRequest,
    UpdateCategoryRequest,
)


class CategorySchema(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)


class CreateCategorySchema(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        return CreateCategoryRequest(**validated_data)


class UpdateCategorySchema(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        return UpdateCategoryRequest(**validated_data)


class GetCategoryByIdSchema(serializers.Serializer):
    id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return GetCategoryByIdRequest(**validated_data)


class FindCategoriesSchema(serializers.Serializer):
    search = serializers.CharField(required=True, max_length=200)

    def create(self, validated_data):
        return FindCategoriesRequest(**validated_data)


class DeleteCategorySchema(serializers.Serializer):
    id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return DeleteCategoryRequest(**validated_data)
