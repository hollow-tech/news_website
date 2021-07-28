from django.views.generic import ListView, DetailView
from hitcount.views import HitCountDetailView
from taggit.models import Tag
from .models import News


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class NewsIndexView(TagMixin, ListView):
    model = News
    template_name = 'news_list.html'
    queryset = News.objects.all()
    context_object_name = 'news_list'


class TagIndexView(TagMixin, ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class NewsDetailView(HitCountDetailView):
    model = News
    template_name = 'news_detail.html'
    queryset = News.objects.all()
    slug_field = "slug"
    count_hit = True
