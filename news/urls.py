from django.urls import path
from .views import NewsIndexView, TagIndexView, NewsDetailView


urlpatterns = [
    path('', NewsIndexView.as_view(), name='home'),
    path('tags/<slug:tag_slug>', TagIndexView.as_view(), name='news_by_tag'),
    path("<slug:slug>/", NewsDetailView.as_view(), name="news_detail"),
]
