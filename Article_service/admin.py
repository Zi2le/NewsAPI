from django.contrib import admin
from .models import Tag,Post,Category,Continent,Country

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Continent)

