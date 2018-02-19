from django.contrib import admin
from .models import Post, Category, Episode, Show
from django_summernote.admin import SummernoteModelAdmin
from sorl_cropping import ImageCroppingMixin


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, SummernoteModelAdmin):
    list_display = ('title', 'show', 'publish_at', 'deleted')
    list_filter = ('deleted', 'publish_at', 'show')

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.show:
            show_episodes = Episode.objects.filter(show=obj.show)
            form.base_fields['episodes'].queryset = show_episodes
        return form


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    pass


@admin.register(Show)
class ShowAdmin(SummernoteModelAdmin):
    list_display = ('name', 'archived')
    list_filter = ('archived', )
    ordering = ('archived', 'name')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at')
    list_filter = ('show', )
