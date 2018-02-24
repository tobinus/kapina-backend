from django.conf.urls import url, include
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
