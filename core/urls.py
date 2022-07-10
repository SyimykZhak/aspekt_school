from django.urls import path
from . import views

urlpatterns=[
    path('', views.MainListView.as_view(), name='main'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('form', views.QustionsView.as_view(), name='question_view'),
]

