from django.shortcuts import render, Http404, get_object_or_404
from django.views.generic.edit import UpdateView, CreateView
from data_models.models import Post, Show, Episode


menus = [
    { 'name': 'shows', 'text': 'Alle show', 'url_name': 'shows' },
    { 'name': 'episodes', 'text': 'Alle episoder', 'url_name': 'episodes' },
    { 'name': 'posts', 'text': 'Alle poster','url_name': 'posts' },
    { 'name': 'images', 'text': 'Bilder','url_name': 'images' },
]

def get_base_context():
    return {
        'shows': Show.objects.all()[:20],
        'episodes': Episode.objects.all()[:20],
        'posts': Post.objects.all(),
        'menus': menus,
    }


def AdminIndexView(request):
    context = get_base_context()
    return render(request, 'admin/admin_index.html', context)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'admin/detailviews/post_detail.html'
    fields = []

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        return context


class ShowUpdateView(UpdateView):
    model = Show
    template_name = 'admin/detailviews/show_detail.html'
    fields = []

    def get_context_data(self, **kwargs):
        context = super(ShowUpdateView, self).get_context_data(**kwargs)
        context.update(get_base_context())
        return context


def detailView(model, template_name):
    def viewMethod(request, pk):
        object = get_object_or_404(Episode, pk=pk)
        context = get_base_context()
        context['object'] = object
        return render(request, template_name, context)
    return lambda request, pk: viewMethod(request, pk)

episodeUpdateView = detailView(Episode, 'admin/detailviews/episode_detail.html')

def allShowsView(request):
    context = get_base_context()
    return render(request, 'admin/admin_shows.html', context)

def allEpisodesView(request):
    context = get_base_context()
    return render(request, 'admin/admin_shows.html', context)

def allPostsView(request):
    context = get_base_context()
    return render(request, 'admin/admin_shows.html', context)