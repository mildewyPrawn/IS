from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),
    # path('about/', TemplateView.as_view(template_name='about')),
    path('about/', views.About.as_view(), name='about'),
]
