from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from sorl_cropping import ImageCroppingMixin

from .models import Category, Settings, Episode, Post, Show


class ShowFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        shows = Show.objects.filter(archived=self.archived)
        return [(show.id, str(show)) for show in shows]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(show=self.value())
        else:
            return queryset


class ActiveShowFilter(ShowFilter):
    title = 'aktive programmer'
    parameter_name = 'show'
    archived = False


class ArchivedShowFilter(ShowFilter):
    title = 'arkiverte programmer'
    parameter_name = 'show'
    archived = True


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, SummernoteModelAdmin):
    list_display = ('title', 'show', 'publish_at', 'deleted')
    list_filter = ('deleted', 'publish_at', 'show')
    search_fields = ('title', 'show__name')

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.show:
            show_episodes = Episode.objects.filter(show=obj.show)
            form.base_fields['episodes'].queryset = show_episodes
        return form


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    pass

@admin.register(Settings)
class SettingsAdmin(SummernoteModelAdmin, SingletonModelAdmin):
    pass


@admin.register(Show)
class ShowAdmin(SummernoteModelAdmin):
    list_display = ('name', 'archived')
    list_filter = ('archived', )
    ordering = ('archived', 'name')
    search_fields = ('name', )


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at')
    list_filter = (ActiveShowFilter, ArchivedShowFilter)
    search_fields = ('title', 'show__name')
