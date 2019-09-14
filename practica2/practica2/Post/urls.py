from django.urls import include, path
from .views import HomePageView, OnePost
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='onePost'),
    path('<int:post_id>/', OnePost.as_view(), name='onePost'),
]
