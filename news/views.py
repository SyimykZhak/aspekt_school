from django.views.generic import ListView, DetailView
from .models import *
from django.core.paginator import Paginator
# Create your views here.

class NewsListView(ListView):
    model = News
    template_name ='news/news.html'
    context_object_name = "news"
    queryset = News.objects.filter(draft = False)
    ordering = ['-add_time']
    paginate_by = 1

   
    

class NewsDetailView(DetailView):
    model = News
    template_name ='news/new.html'
    context_object_name = "new"
    slug_field = "url"
    
    
    


class CategooryDetalView(DetailView):
    model = Category
    template_name = 'news/category.html'
    context_object_name = "category"
    slug_field = "url"
    ordering = ['-add_time']
    paginate_by = 10

    #  def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context