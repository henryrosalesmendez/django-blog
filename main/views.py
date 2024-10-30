from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Article, Tag
from .utils import get_articles_by_year

class ListView(ListView):
    model = Article
    template_name = 'main/list.html'
    context_object_name = 'articles_by_year'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content_title"] = "Posts by Year"
        return context

    def get_queryset(self, *args, **kwargs):

        articles = []
        if self.request.user.is_authenticated:
            articles = Article.objects.all().order_by('-created_at')
        else:
            articles = Article.objects.filter(public=True).order_by('-created_at')

        return get_articles_by_year(articles)
    

class ArticleView(TemplateView):

    slug_url_kwarg = "article_slug"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        slug = self.kwargs.get(self.slug_url_kwarg)
        print(f"{slug=}")
        article = Article.objects.filter(slug=slug).first()
        print(f"{article=}")
        if article is None or (not article.public and not request.user.is_authenticated):
            return render(request=request, template_name="404.html", context={})
        context = {
            "article": article,
        }
        print(f"{article.template_filename=}")
        return render(request=request, template_name=article.template_filename, context=context)



class TagView(TemplateView):

    slug_url_kwarg = "tag_name"
    template_name = 'main/list.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:

        print("inside tag view")

        # getting tag name from url
        tag_name = self.kwargs.get(self.slug_url_kwarg)
        tag: Tag | None = Tag.objects.filter(name=tag_name).first()
        if tag is None:
            return render(request=request, template_name="404.html", context={})
        print(f"{tag=}")
        
        # getting articles with the tag
        articles = []
        if self.request.user.is_authenticated:
            articles = Article.objects.filter(tags__in = [tag]).order_by('-created_at')
        else:
            articles = Article.objects.filter(tags__in = [tag], public=True).order_by('-created_at')
        print(f"{articles=}")
        
        # getting articles by year
        articles_by_year = get_articles_by_year(articles)
        context = {
            "articles_by_year": articles_by_year,
            "content_title" : f"Posts about <i>#{tag_name}</i>",
        } 
        return render(request=request, template_name=self.template_name, context=context)