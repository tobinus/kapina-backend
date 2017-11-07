from django.conf.urls import url, include
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static
from app.views import AdminIndexView, PostUpdateView, ShowUpdateView, episodeUpdateView, allEpisodesView, allPostsView, allShowsView

admin_urls = [
    url(r'^posts/', allPostsView, name='posts'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostUpdateView.as_view(), name='post_detail'),
    url(r'^shows/', allShowsView, name='shows'),
    url(r'^show/(?P<slug>[-\w]+)/$', ShowUpdateView.as_view(), name='show_detail'),
    url(r'^episodes/', allEpisodesView, name='episodes'),
    url(r'^episode/(?P<pk>[-\w]+)/$', episodeUpdateView, name='episode_detail'),
    url(r'^images/', allPostsView, name='images'),
    url(r'$', AdminIndexView, name='admin_index'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^graphql', include('api_graphql.urls')),
    url(r'^graphiql', include('django_graphiql.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^newadmin/', include(admin_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
