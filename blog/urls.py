from django.urls import path, include
from django.views.generic.detail import DetailView
from .views import Index, Detail

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
]
