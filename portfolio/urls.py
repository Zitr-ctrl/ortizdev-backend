from django.urls import path
from .views import hello, get_projects

urlpatterns = [
    path("hello/", hello),
    path("projects/", get_projects),
]
