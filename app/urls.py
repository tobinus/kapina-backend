from django.conf.urls import url, include
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^graphql', include('api_graphql.urls')),
    url(r'^graphiql', include('django_graphiql.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
