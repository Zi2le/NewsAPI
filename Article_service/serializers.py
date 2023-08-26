from rest_framework import serializers
from .models import Post, Tag,Continent,Country,Category



class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = (
        "id",
        "tag"
    )
class ContinentSerializer(serializers.ModelSerializer):
    model = Continent
    fields = (
        "id",
        "continent"
    )
class CountrySerializer(serializers.ModelSerializer):
    model = Country
    fields = (
        "id",
        "country"
    )
class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = (
        "id",
        "category"
    )        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "Headline",
            "Description",
            "Author",
            "publication_Date",
            "url",
            "thumbnail",
            "content",
            "continent",
            "country",
            "category",
            "tag"
        )
