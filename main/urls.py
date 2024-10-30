from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "article"

urlpatterns = [
    path('list', views.ListView.as_view(), name='list'),
    path('tag/<slug:tag_name>', views.TagView.as_view(), name='tag'),
    path('<slug:article_slug>', views.ArticleView.as_view(), name='post'),
]

