from django.contrib import admin
from .models import Post, Category, Episode, Show
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    pass


@admin.register(Show)
class ShowAdmin(SummernoteModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
