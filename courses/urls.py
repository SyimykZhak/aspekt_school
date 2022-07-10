from django.urls import path
from . import views

urlpatterns=[
    path('', views.CoursesListView.as_view(), name='coursess'),
    path('<slug:slug>/', views.CoursesDetailView.as_view(), name='course'),
    path('register/<int:pk>', views.RegisterView.as_view(), name='register_view'),
]
