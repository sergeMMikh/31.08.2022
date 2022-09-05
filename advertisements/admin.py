from django.contrib import admin
from .models import AdvertisementStatusChoices, Advertisement


@admin.register(Advertisement)
class ArticleAdmin(admin.ModelAdmin):
    ...
