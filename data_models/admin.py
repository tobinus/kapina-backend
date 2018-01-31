from django.contrib import admin
from .models import Post, Category, Episode, Show
from django_summernote.admin import SummernoteModelAdmin
from sorl.thumbnail.admin import AdminImageMixin


@admin.register(Post)
class PostAdmin(AdminImageMixin, SummernoteModelAdmin):
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
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
