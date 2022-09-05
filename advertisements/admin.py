from django.contrib import admin
from .models import Advertisement
from .serializers import UserSerializer


@admin.register(Advertisement)
class ArticleAdmin(admin.ModelAdmin):
    ...


# @admin.register(UserSerializer)
# class ArticleAdmin(admin.ModelAdmin):
#     ...
