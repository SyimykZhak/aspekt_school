from django.urls import path
from . import views

urlpatterns=[
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path("category/<slug:slug>/", views.CategooryDetalView.as_view(), name="category_detail"),
]